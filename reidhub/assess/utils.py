"""
This module contains some helper functions for common operations in the assess stage

"""

import os
import time
import logging
from pathlib import Path
from typing import List, Union
import fiftyone as fo
import fiftyone.operators as foo
import fiftyone.plugins as fop
import fiftyone.brain as fob

from ..access.utils import find_images


IMAGE_ISSUES_OPERATIONS = [
    "compute_aspect_ratio",
    "compute_brightness",
    "compute_contrast",
    "compute_exposure",
    "compute_saturation",
    "compute_vignetting",
    "compute_blurriness",
    "compute_entropy",
]


# count the number of images
def get_number_of_images(dataset_root: str) -> int:
    """
    Get the number of images in a dataset from its root path

    Args:
        dataset_root (str): The root path of the dataset

    Returns:
        int: Number of images in the directory
    """
    image_paths = find_images(dataset_root)
    return len(image_paths)


# get the size of the dataset
def get_directory_size(dataset_root: Union[str, Path]) -> int:
    """
    Calculate the total size of a directory and its subdirectories in bytes.

    Args:
        dataset_root (str): The root path of the dataset

    Returns:
        int: Total size in bytes, or 0 if directory doesn't exist
    """
    total_size = 0

    try:
        # Walk through directory and subdirectories
        for dirpath, _, filenames in os.walk(dataset_root):
            # Add size of each file
            for filename in filenames:
                file_path = os.path.join(dirpath, filename)
                try:
                    total_size += os.path.getsize(file_path)
                except (OSError, FileNotFoundError):
                    # Skip files that can't be accessed
                    continue

        return total_size

    except (OSError, FileNotFoundError):
        # Return 0 if directory doesn't exist or can't be accessed
        return 0


# Convert bytes to human-readable format
def format_size(size_in_bytes: Union[float, int]) -> str:
    """
    Convert bytes to human-readable format (KB, MB, GB, etc.)

    Args:
        size_in_bytes (int): Size in bytes

    Returns:
        str: Formatted size string
    """
    for unit in ["B", "KB", "MB", "GB", "TB"]:
        if size_in_bytes < 1024:
            return f"{size_in_bytes:.2f} {unit}"
        size_in_bytes /= 1024
    return f"{size_in_bytes:.2f} PB"


# check for duplicates
def check_for_duplicates(dataset: fo.Dataset) -> fo.Dataset:
    """
    Compute uniqueness of dataset samples and check for duplicates

    Args:
        dataset (fo.Dataset): the dataset to check for duplicates.

    Returns:
        fo.Dataset: the dataset with the `uniqueness` and `duplicates` fields added

    """
    fob.compute_uniqueness(dataset)

    # check for near duplicates
    index = fob.compute_near_duplicates(dataset)
    dups_view = index.duplicates_view()
    dups_view.tag_samples("duplicate")

    return dataset


# Check for image quality issues
async def fiftyone_check_image_quality_issues(
    dataset: fo.Dataset,
    operations: List[str] = IMAGE_ISSUES_OPERATIONS,
) -> fo.Dataset:
    """
    compute potential image quality issues such as brightness, contrast, exposure using\
    the image_quality_issues operator by jacob marks:

    Args:
        dataset (fo.Dataset): fiftyone dataset to compute image issues for
        operations (list(str)): list of operations to compute for the dataset

    Returns:
        (fo.Dataset): fiftyone dataset with image issues computed
    """

    # Download image issues plugin from github repository
    fop.download_plugin("https://github.com/jacobmarks/image-quality-issues/")

    for operation in operations:
        logging.info(f"Executing {operation} operation")
        start_time = time.time()
        operator = foo.get_operator(f"@jacobmarks/image_issues/{operation}")
        await operator(dataset)
        end_time = time.time()
        dataset.save()
        logging.info(
            f"Execution time: {end_time - start_time:.2f} seconds ({operation} operation)"
        )
    return dataset
