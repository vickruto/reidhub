import os
import yaml
from typing import Dict
from .models import DatasetConfig

# Path to the YAML file
DATASET_YAML_PATH = os.path.join(os.path.dirname(__file__), '../../config/datasets.yaml')

def load_datasets(file_path: str) -> Dict[str, DatasetConfig]:
    """
    Loads datasets from a YAML file and returns them as DatasetConfig objects.
    """
    with open(file_path, 'r') as file:
        data = yaml.safe_load(file)

    datasets = {}
    for dataset_name, dataset_data in data.items():
        datasets[dataset_name] = DatasetConfig(**dataset_data)

    return datasets

'''
def get_dataset_config(DATASET_ID: str):
    """
    Loads the dataset configuration for a given dataset name.
    """
    datasets = load_datasets(DATASET_YAML_PATH)
    return datasets.get(DATASET_ID)  # add a None return option
'''


def get_dataset_config(DATASET_ID: str):
    """
    Loads the dataset configuration for a given dataset name.
    """
    with open(DATASET_YAML_PATH, 'r') as file:
        datasets = yaml.safe_load(file)

    dataset_data = datasets.get(DATASET_ID)
    dataset_data = DatasetConfig(**dataset_data)

    return dataset_data  # add a None return option
