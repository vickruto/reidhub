import logging
import time
import pandas as pd
from pathlib import Path
import fiftyone as fo
import fiftyone.operators as foo
import fiftyone.plugins as fop
from typing import List, Optional, Union
from ..config import config


def find_images(root_path: Union[str, Path]) -> List[Path]:
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
    fields: Optional[List[str]] = None,
) -> fo.Dataset:
    """
    creates a fiftyone dataset
    Args:
        root_path (str) : the root of the dataset containing the images <- also allow pathlib Paths
        metadata_df (pd.DataFrame) : the metadata for the dataset. Should have the columns (identity, image_path, image_type,)
        dataset_name (str) : The name of the fiftyone dataset created
        fields (list of str) : list of fields required in the fiftyone dataset created. should be existing columns in the metadata_df. \
                Default : None : Use all the columns in the metadata_df
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
        sample = fo.Sample(**row._asdict())
        samples.append(sample)

    # Create dataset from samles
    dataset = fo.Dataset(dataset_name, overwrite=True)
    _ = dataset.add_samples(samples)
    dataset.compute_metadata()
    dataset.persistent = True
    dataset.save()
    return dataset
