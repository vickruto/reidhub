"""
This module contains some helper functions for common operations in the assess stage

"""
from typing import List
import fiftyone as fo
import fiftyone.operators as foo
import fiftyone.plugins as fop

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


# get the size of the dataset


# check for duplicates


# ############################# ADVANCED ##########################################

# check for near duplicates

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
