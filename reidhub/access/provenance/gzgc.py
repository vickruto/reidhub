"""
This module downloads the Great Zebra and Giraffe Count (GZGC) Dataset \
    from a GCP Bucket provided by Lila Datasets

"""

# todos:
# Refactor this function later to do the following:
# 1) use a reidhub cache folder
# 2) remove the zip/tar file after downloading and unzipping successfully

import os
import json
import pandas as pd
from pathlib import Path
import logging
import requests
import tarfile

from .dataset_parser import get_dataset_config
from ...config import config as defaults

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
    dataset_dir = Path(defaults['cache_root']) / DATASET_ID
    dataset_dir = dataset_dir.expanduser().resolve()
    tar_path = dataset_dir / filename
    dataset_dir.mkdir(parents=True, exist_ok=True)

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


def systematize_dataset_metadata(dataset_root:str) -> pd.DataFrame:
    '''
    Systematize dataset metadata for the Great Zebra and Giraffe Count and ID dataset
    Args: 
        dataset_root (str) : The root path containing the extracted dataset

    Returns:
        pd.DataFrame: output dataframe containing systematized metadata
    '''
    annotations_root = Path(dataset_root) / 'gzgc.coco' / 'annotations'

    # The train split annotations file contains all the information we need about the dataset
    train_annotations_path = annotations_root / 'instances_train2020.json'
    with open(train_annotations_path) as f:
        train_annots = json.loads(f.read())
    
    # gather information from the train split annotation file
    train_images_df = pd.DataFrame(train_annots['images'])
    train_annotations_df = pd.DataFrame(train_annots['annotations'])
    license_mapping = {i['id']: i['url'] for i in train_annots['licenses']}
    category_mapping = {i['id']: i['name'] for i in train_annots['categories']}

    # process the information & systematize
    metadata_df = train_annotations_df.merge(train_images_df, left_on='image_id', right_on='id')
    metadata_df['license'] = metadata_df['license'].map(license_mapping)
    metadata_df['species'] = metadata_df['category_id'].map(category_mapping)
    
    # get image paths relative to the dataset root
    images_relative_root = os.path.join('gzgc.coco', 'images', 'train2020')
    metadata_df['filepath'] = metadata_df['file_name'].apply(lambda x : os.path.join(images_relative_root, x))
    
    # Assert that all the relative image paths created exist
    assert metadata_df['filepath'].apply(lambda x : os.path.exists(os.path.join(dataset_root, x))).all(), 'Some of the image paths reference paths that do not exist'
    
    
    # Filter for necessary columns and rename columns to standardized naming convention
    retain_cols = ['filepath', 'bbox', 'viewpoint', 'species', 'identity', 'license', 'height', 'width', 'photographer', 
                   'timestamp', 'latitude', 'longitude', 'secondary_identities', 'image_id']
    
    column_mappings = {
        'name': 'identity',
        'date_captured': 'timestamp',
        'gps_lat_captured': 'latitude',
        'gps_lon_captured': 'longitude',
        'individual_ids': 'secondary_identities'
    }
    
    metadata_df = metadata_df.rename(columns=column_mappings)
    metadata_df = metadata_df[retain_cols].copy()
    
    return metadata_df