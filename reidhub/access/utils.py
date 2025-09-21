import logging
import time
import pandas as pd
import fiftyone as fo
import fiftyone.operators as foo
from typing import List, Optional
from ..config import config

from pathlib import Path

operations = [
    'compute_aspect_ratio',
    'compute_brightness',
    'compute_contrast',
    'compute_exposure',
    'compute_saturation',
    'compute_vignetting',
    'compute_blurriness',
    'compute_entropy',
]


def find_images(root_path):
    """
    Find images in all the subdirectories of a given path
    Args:
        root_path (str): Path to the root directory
    Returns:
        image_files (list): List of image files
    """
    root_path = Path(root_path)
    image_files = [
        path
        for path in root_path.rglob("*.*")
        if path.suffix[1:].lower() in config["IMG_FORMATS"]
    ]
    return image_files


def create_fiftyone_dataset(
    root_path: str,
    metadata_df: pd.DataFrame,
    dataset_name: str,
    fields: Optional[List[str]]=None,
) -> fo.Dataset:
    """
    creates a fiftyone dataset
    Args:
        root_path (str) : the root of the dataset containing the images <- also allow pathlib Paths
        metadata_df (pd.DataFrame) : the metadata for the dataset. Should have the columns (identity, image_path, image_type,)
        fields (list of str) : list of fields required in the fiftyone dataset created. should be existing columns in the metadata_df. \
                Default : None : Use all the columns in the metadata_df
        dataset_name (str) : The name of the fiftyone dataset created
    Returns:
        fo.Dataset: Fiftyone dataset
    """
    # Find all the images in the root_path and its subdirectories
    # image_paths = find_images(root_path)

    metadata_df["filepath"] = metadata_df["filepath"].apply(
        lambda x: Path(root_path) / x
    )

    if fields:
        # TODO: assert all fields are valid (ie they exist in the metadata dataframe)
        #
        if "filepath" not in fields:
            fields += "filepath"  # filepath is required to create the dataset.
        metadata_df = metadata_df[fields].copy()

    # Create samples
    samples = []
    for row in metadata_df.itertuples():
        sample = fo.Sample( **row._asdict())
        samples.append(sample)

    # Create dataset from samles
    dataset = fo.Dataset(dataset_name, overwrite=True)
    _ = dataset.add_samples(samples)
    dataset.compute_metadata()
    dataset.persistent = True
    dataset.save()
    return dataset


def fiftyone_check_image_quality_issues(
    dataset:fo.Dataset,
    operations:List[str],
) -> fo.Dataset
    '''
    compute potential image quality issues such as brightness, contrast, exposure using\
    the image_quality_issues operator by jacob marks:

    Args:
        dataset (fo.Dataset): fiftyone dataset to compute image issues for
        operations (list(str)): list of operations to compute for the dataset

    Returns:
        (fo.Dataset): fiftyone dataset with image issues computed
    '''
    for operation in operations:
        logging.info(f"Executing {operation} operation")
        start_time = time.time()
        operator = foo.get_operator(f"@jacobmarks/image_issues/{operation}")
        await operator(dataset)
        end_time = time.time()
        dataset.save()
        logging.info(f"Execution time: {end_time - start_time:.2f} seconds ({operation} operation)")
    return dataset