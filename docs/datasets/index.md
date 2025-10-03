# Datasets

The **Datasets** section contains detailed documentation for each re-identification dataset supported in `reidhub`.  

---

Each dataset page provides:  


**🗒️ High-level information** — quick facts eg number of images & identities, dataset size, species present and conservation status, license, etc.

**🖼️ Sample Image Grid** — a quick visual glimpse of the dataset (especially useful if you’re not familiar with the species).

**📖 Overview** — general background on the dataset.

**📥 Access instructions** — how to download and prepare the dataset.

**🗂 Standardized metadata** — the unified dataframe schema (metadata_df) used across all datasets.

**🧩 Enrichments** — additions made to the dataset to make it more usable.

**🔗 Mirror links** — alternative download mirrors.

**🔍 Usage notes** — quirks, preprocessing steps, or caveats specific to the dataset.

**📊 Example workflows** — sample code showing how to integrate the dataset with reidhub.

**📑 Citation** — how to cite the dataset.

**📚 Publications** — short summaries of related research using the dataset.

**💡 Potential use cases** — potential applications of the dataset to be explored.


---

## Supported Datasets

<!--TODO: 
MAKE THIS TABLE AUTO-FILLING USING JINJA
-->
| Dataset                        | Species Covered                          | Highlights                                   |
|--------------------------------|------------------------------------------|----------------------------------------------|
| [Great Zebra and Giraffe Count (GZGC)](./gzgc.md) | Plains zebra, Masai Giraffe     | Two days censusing exercise at Nairobi National Park |
| Nyala Data                     | Nyala                                    | Field imagery dataset focused on nyala re-identification |
| Amur Tigers Re-identification  | Amur Tiger                               | Images sampled from videos captured at a conservancy in China |

!!! note
    More datasets upcoming


---

## General Workflow

Regardless of dataset, the general usage pattern is the same:  

Example with [`gzgc`](../datasets/gzgc.md) dataset:  
```python
from reidhub.access.provenance.gzgc import download_and_extract
dataset_root = download_and_extract()
print(f'Dataset downloaded to: {dataset_root}')
```

Likewise, for any other dataset already added to `reidhub`, you can access it by replacing the dataset slug(identifier) ie `gzgc`.  
For example, for `Nyala Data`, you just replace `gzgc` with `nyala`:

```python
from reidhub.access.provenance.nyala import download_and_extract
dataset_root = download_and_extract()
print(f'Dataset downloaded to: {dataset_root}')
```

<!--TODO: MAKE IT SOMETHING LIKE
    import reidhub as rh
    
    # Example: Access the GZGC dataset
    dataset = rh.access("gzgc")
    
    # Standardize to a common metadata format (metadata_df)
    df = rh.assess(dataset)
    print(df.head())
-->

---

## Adding Your Own Dataset

`reidhub` will continue to strive to be extensible.  
If a dataset you know of isn’t included yet, don't worry, a more user-friendly custom dataset loading functionality will be added soon. 

Soon, you will be able to add a new dataset to the package hands off using a customized Github Pull Requests template. 

Watch out for the [Contributing guide](../pages/contributing.md#adding-a-new-dataset).  

---

✨ Head over to the individual dataset pages in the sidebar to dive into details.  