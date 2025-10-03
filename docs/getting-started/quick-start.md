# Quick Start

This short guide will help you get up and running with **reidhub** in just a few steps.  
It will show you how to access a dataset, standardize its metadata, and inspect the results.

## 1. Installation

Make sure you’ve already installed `reidhub`. If not, check out the [Installation guide](./installation.md).

---

## 2. Accessing a Dataset

With `reidhub`, you can download and access re-identification datasets in a unified way.

Example with [`gzgc`](../datasets/gzgc.md) dataset:  
```python
from reidhub.access.provenance.gzgc import download_and_extract
dataset_root = download_and_extract()
print(f'Dataset downloaded to: {dataset_root}')
```


<!-- TODO: refactor the code to put together acess components 
Example:

    import reidhub as rh

    # Access the Market-1501 dataset (downloads if not already cached)
    dataset = rh.access("market1501")
-->

These commands will:

- Download the [Great Zebra and Giraffe Count and ID Dataset](https://lila.science/datasets/great-zebra-giraffe-id) dataset (if not already present).  
- Cache it locally for reuse.  
- Return a path to the local dataset cache <!--TODO: (perhaps refactor to instead return) ... a dataset object you can work with.-->

---

## 3. Standardizing Metadata

Different datasets often have different formats.  
`reidhub` automatically unifies them into a **standardized metadata dataframe**.

Example with [`gzgc`](../datasets/gzgc.md) dataset:  
```python
from reidhub.access.provenance.gzgc import systematize_dataset_metadata

# Convert dataset into a standardized dataframe
metadata_df = systematize_dataset_metadata(dataset_root)

# Preview output metadata
metadata_df.head()
```


---

## 4. Enriching Datasets
To make the datasets more usable and make ideating much easier, we generate useful reusable artifacts.  
For animal re-identification datasets, these include:  
    1. MegaDetector predictions  
    2. SAM segmentations  
    3. Open Clip Embeddings  
    4. Siglip Embeddings  
    5. DinoV3 embeddings  
    5. Spatial feature embeddings eg NVidia C-Radiov3 model embeddings    
etc...  

<p align="center">
  <img src="../assets/content_Under-Construction-Free-Download-PNG.png" alt="In development" width="120"/>
</p>


## 5. Re-Access

After initial access of the datasets in the earlier stages and then enriching it, we cache the datasets together with the enrichments and push them to open data repositories including `Hugging Face`, `Kaggle` and `DagsHub` where we can re-access and reuse them. 


<p align="center">
  <img src="../assets/content_Under-Construction-Free-Download-PNG.png" alt="In development" width="120"/>
</p>


<!--TODO: implement:
Example:

    # Example: attach embeddings or predictions to the dataset
    enriched = rh.enriched(dataset, artifacts={
        "embeddings": "path/to/embeddings.npy",
        "preds": "path/to/preds.json"
    })
-->

---

## 5. What’s Next?

- Explore the [Access Framework](../api/access.md) to understand provenance and enrichment.  
- Browse the [Supported Datasets](../datasets/index.md#supported-datasets) page for a full list.  
- Check out the [Example Tutorials](../tutorials/index.md) for end-to-end workflows.

---

🚀 That’s it — you’ve just accessed and standardized your first dataset with `reidhub`!

!!! note
    The `reidhub` project is still in its early stages of development and is actively being developed.   
    Check back later for new exciting features.  
