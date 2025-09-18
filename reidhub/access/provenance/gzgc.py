"""
This module downloads the Great Zebra and Giraffe Count (GZGC) Dataset \
    from a GCP Bucket provided by Lila Datasets

"""

# todos:
# Refactor this function later to do the following:
# 1) use a reidhub cache folder
# 2) remove the zip/tar file after downloading and unzipping successfully

from pathlib import Path
import logging
import requests
import tarfile

from .dataset_parser import get_dataset_config
from ...config import cache_root

# Dataset Identifier
DATASET_ID = "gzgc"


def download_and_extract() -> str:
    """
    downloads the gzgc from the gcp bucket url provided by lila datasets.
    Accessible here: https://lila.science/datasets/great-zebra-giraffe-id

    Args:
        DATASET_ID: str :- the identifier for the dataset.

    returns:
        a path to the extracted and formatted `reidhub` dataset
    """
    config = get_dataset_config(DATASET_ID)
    url = config.url[0]
    filename = url.split("/")[-1]

    # Create dataset-specific cache directory
    dataset_dir = Path(cache_root) / DATASET_ID
    dataset_dir.mkdir(parents=True, exist_ok=True)

    tar_path = dataset_dir / filename

    # Download the file if not already present
    if not tar_path.exists():
        logging.info(f"Downloading {filename} to {tar_path}...")
        try:
            response = requests.get(url, stream=True)
            response.raise_for_status()
            with open(tar_path, "wb") as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
            logging.info(f"Download complete: {tar_path}")
        except requests.exceptions.RequestException as e:
            logging.error(f"Error downloading {filename}: {e}")
            return str(dataset_dir)
    else:
        logging.info(f"{tar_path} already exists. Skipping download.")

    # Extract the file into the dataset directory
    extracted_flag = dataset_dir / ".extracted"
    if not extracted_flag.exists():
        logging.info(f"Extracting {tar_path} into {dataset_dir}...")
        try:
            with tarfile.open(tar_path, "r:gz") as tar:
                tar.extractall(path=dataset_dir)
            extracted_flag.touch()  # mark extraction complete
            logging.info("Extraction complete.")
        except tarfile.TarError as e:
            logging.error(f"Error extracting {tar_path}: {e}")
    else:
        logging.info(f"Extraction already completed for {tar_path}.")

    return str(dataset_dir)
