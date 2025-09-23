"""
This module contains functions that are useful for generatic static objects for assessing reid datasets
Examples: Sample images grid
          Identity distributions
          etc

"""

from collections import Counter
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
from PIL import Image
from matplotlib.cm import get_cmap
from typing import List, Union, Tuple, Sequence


def plot_grid(
    images: List[Union[np.ndarray, Image.Image]],
    ids: List[int],
    grid_shape: Tuple[int, int] = (3, 3),
    img_size: Tuple[int, int] = (224, 224),
    spacing: float = 0.05,
) -> plt.Figure:
    """
    Plot a grid of images with colored borders per identity.

    Args:
        images (List[Union[np.ndarray, PIL.Image.Image]]): List of images (either numpy arrays or PIL images).
        ids (List[int]): List of identity labels corresponding to each image.
        grid_shape (Tuple[int, int], optional): Shape of the grid as (rows, cols). Default is (3, 3).
        img_size (Tuple[int, int], optional): The (height, width) to resize the images. Default is (224, 224).
        spacing (float, optional): Fractional spacing between subplots. Default is 0.05.

    Returns:
        (matplotlib.figure.Figure): The figure containing the grid of images with borders.

    Examples:
        >>> import numpy as np
        >>> from PIL import Image
        >>> images = [np.random.randint(0, 255, (100, 100, 3), dtype=np.uint8) for _ in range(9)]
        >>> ids = [1, 1, 2, 2, 3, 3, 4, 4, 5]
        >>> fig = plot_grid(images, ids, grid_shape=(3, 3), img_size=(100, 100), spacing=0.1)
        >>> plt.close(fig)  # Close the figure to prevent display in non-interactive environments
    """
    # Unpack grid shape
    cols, rows = grid_shape

    # Calculate total number of cells in the grid
    n = rows * cols

    # Sample n images if more are provided
    if len(images) > n:
        idxs = np.random.choice(len(images), n, replace=False)
        images = [images[i] for i in idxs]
        ids = [ids[i] for i in idxs]

    # Normalize identities into a color map
    unique_ids = sorted(set(ids))
    cmap = plt.cm.get_cmap("tab20", len(unique_ids))  # Updated cmap access
    id2color = {uid: cmap(i) for i, uid in enumerate(unique_ids)}

    # Create subplots
    fig, axes = plt.subplots(rows, cols, figsize=(cols * 2.5, rows * 2.5))
    axes = np.array(axes).reshape(rows, cols)

    # Set transparent background
    fig.patch.set_alpha(0)

    # Plot each image with its border
    for ax, img, identity in zip(axes.flatten(), images, ids):
        # Convert to PIL Image if necessary and resize
        if not isinstance(img, Image.Image):
            img = Image.fromarray(img)
        img_resized = img.resize(img_size)

        # Display image
        ax.imshow(img_resized)
        ax.axis("off")

        # Draw border around the image
        rect = patches.Rectangle(
            (0, 0),
            img_size[0],
            img_size[1],
            linewidth=10,
            edgecolor=id2color[identity],
            facecolor="none",
            transform=ax.transData,
        )
        ax.add_patch(rect)

    # Remove extra axes if fewer images are provided
    for ax in axes.flatten()[len(images) :]:
        ax.axis("off")

    # Adjust spacing between subplots
    plt.subplots_adjust(wspace=spacing, hspace=spacing)

    return fig


# def plot_identity_histogram(ids, bins=50, log_scale=False, alpha=0.6, figsize=(8, 5)):
"""
Plot a transparent histogram of identity frequencies 
(how many images per identity).

Args:
    ids (list): List of identity labels.
    bins (int or list): Number of bins or explicit bin edges.
    log_scale (bool): Whether to use log scale for y-axis.
    alpha (float): Transparency of histogram bars (0=fully transparent, 1=opaque).
    figsize (tuple): Figure size.
    Union[int, Sequence[float], str, None]
"""


def plot_identity_histogram(
    ids: List[Union[int, str]],
    bins: Union[int, Sequence[float]] = 50,
    log_scale: bool = False,
    alpha: float = 0.6,
    figsize: Tuple[float, float] = (8, 5),
) -> plt.Figure:
    """Plot a transparent histogram of identity frequencies (how many images per identity).

    Args:
        ids: List of identity labels (e.g., integers or strings).
        bins: Number of bins or explicit bin edges for the histogram. Defaults to 50.
        log_scale: Whether to use a logarithmic scale for the y-axis. Defaults to False.
        alpha: Transparency of histogram bars (0=fully transparent, 1=opaque). Defaults to 0.6.
        figsize: Figure size as (width, height) in inches. Defaults to (8, 5).

    Returns:
        matplotlib.pyplot.Figure: The generated histogram figure.

    Examples:
        >>> ids = ["zebra1", "zebra1", "zebra2", "zebra3", "zebra3", "zebra3"]
        >>> fig = plot_identity_histogram(ids, bins=3, log_scale=False, alpha=0.7, figsize=(6, 4))
        >>> plt.close(fig)  # Close the figure to prevent display in non-interactive environments
    """
    # Count how many images per identity
    counts = list(Counter(ids).values())

    # Plot histogram
    fig, ax = plt.subplots(figsize=figsize)
    ax.hist(counts, bins=bins, color="steelblue", edgecolor="black", alpha=alpha)

    # Transparent backgrounds
    fig.patch.set_alpha(0)  # Figure background
    ax.patch.set_alpha(0)  # Axes background

    ax.set_xlabel("Number of images per identity")
    ax.set_ylabel("Number of identities")
    ax.set_title("Identity Frequency Distribution")

    if log_scale:
        ax.set_yscale("log")
        ax.set_ylabel("Number of identities (log scale)")

    plt.tight_layout()
    return fig
