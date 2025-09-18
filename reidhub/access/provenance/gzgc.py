'''
This module downloads the Great Zebra and Giraffe Count (GZGC) Dataset \
    from a GCP Bucket provided by Lila Datasets

'''

## todos:
## Refactor this function later to do the following:
## 1) use a reidhub cache folder
## 2) remove the zip/tar file after downloading and unzipping successfully

import os
import logging
import requests
import tarfile

from .dataset_parser import get_dataset_config


## Dataset Identifier
DATASET_ID = 'gzgc'


def download_and_extract() -> str:
    '''
    downloads the gzgc from the gcp bucket url provided by lila datasets. 
    Accessible here: https://lila.science/datasets/great-zebra-giraffe-id

    Args:
        DATASET_ID: str :- the identifier for the dataset.
    
    returns: 
        a path to the extracted and formatted `reidhub` dataset
    '''
    config = get_dataset_config(DATASET_ID)
    url = config['url'][0]
    filename = url.split('/')[-1]

    # Download the file
    if not os.path.exists(filename):
        logging.info(f"Downloading {filename}...")
        try:
            response = requests.get(url, stream=True)
            response.raise_for_status()  # Will raise an exception for HTTP errors
            with open(filename, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
            logging.info(f"Download complete: {filename}")
        except requests.exceptions.RequestException as e:
            logging.error(f"Error downloading {filename}: {e}")
            return
    else:
        logging.info(f"{filename} already exists. Skipping download.")

    # Extract the file
    if os.path.exists(filename):
        logging.info(f"Extracting {filename}...")
        try:
            with tarfile.open(filename, 'r:gz') as tar:
                tar.extractall()  # You can specify a path in extractall() if you need
            logging.info("Extraction complete.")
        except tarfile.TarError as e:
            logging.error(f"Error extracting {filename}: {e}")
    else:
        logging.error(f"Error: {filename} not found for extraction.")

    return filename
