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
import zipfile
from io import BytesIO

from .dataset_parser import get_dataset_config
from ...config import config as defaults


# Dataset Identifier
DATASET_ID = "sea_star_reid"


def download_and_extract() -> str:
    """
    Downloads the dataset zip file from the provided URL and extracts it.

    Args:
        DATASET_ID (str): The identifier for the dataset.

    Returns:
        str: The path to the extracted and formatted `reidhub` dataset.
    """
    config = get_dataset_config(DATASET_ID)
    url = config.url[0]
    filename = url.split("/")[-1]

    # Create dataset-specific cache directory
    dataset_dir = Path(defaults["cache_root"]) / DATASET_ID
    dataset_dir = dataset_dir.expanduser().resolve()
    zip_path = dataset_dir / filename
    dataset_dir.mkdir(parents=True, exist_ok=True)

    # Download the file if not already present
    if not zip_path.exists():
        logging.info(f"Downloading {filename} to {zip_path}...")
        try:
            response = requests.get(url, stream=True)
            response.raise_for_status()
            with open(zip_path, "wb") as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
            logging.info(f"Download complete: {zip_path}")
        except requests.exceptions.RequestException as e:
            logging.error(f"Error downloading {filename}: {e}")
            return str(dataset_dir)
    else:
        logging.info(f"{zip_path} already exists. Skipping download.")

    # Extract the zip file into the dataset directory
    extracted_flag = dataset_dir / ".extracted"
    if not extracted_flag.exists():
        logging.info(f"Extracting {zip_path} into {dataset_dir}...")
        try:
            with zipfile.ZipFile(zip_path, "r") as zip_ref:
                zip_ref.extractall(dataset_dir)
            extracted_flag.touch()  # mark extraction complete
            logging.info("Extraction complete.")
        except zipfile.BadZipFile as e:
            logging.error(f"Error extracting {zip_path}: {e}")
    else:
        logging.info(f"Extraction already completed for {zip_path}.")

    return str(dataset_dir)