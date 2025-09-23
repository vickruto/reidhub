# Reference for `reidhub/access`

## a. Provenance

> **Provenance** *(noun)*  
> *1. The place of origin or earliest known history of something.*  
> *2. **(informal)** The origin story of a dataset.*  


This sub module provides functionality for accessing raw datasets for the first from the original source.  Its functionalities include `downloading`, `systematizing` and `cataloguing` a dataset from its raw form.

---

### Great Zebra and Giraffe Count

#### ::: reidhub.access.provenance.gzgc.download_and_extract

Examples:

```python
from reidhub.access.provenance.gzgc import download_and_extract
download_and_extract()
```

### Nyala Data

#### ::: reidhub.access.provenance.gzgc.download_and_extract 

<!--## Change above!!-->

Examples:

```python
from reidhub.access.provenance.nyala import download_and_extract
download_and_extract()
```


### Sea Star Re-ID 2023

#### ::: reidhub.access.provenance.gzgc.download_and_extract

<!--
Examples:

```python
from reidhub.access.provenance.seastars import download_and_extract
download_and_extract()
```
-->

---
## b. Enriched

> **Enriched** *(adjective)*  
> *1. Made fuller, more valuable, or more informative.*  
> *2. **(informal)** The return journey of a once-accessed and catalogued dataset*

This sub module provides functionality for re-accessing the `processed`, `systematized` and `enriched` versions of the catalogued datasets from online mirrors including `Hugging Face` and `Kaggle`. 


### Great Zebra and Giraffe Count
#### ::: reidhub.access.provenance.gzgc.download_and_extract

Examples:

```python
from reidhub.access.enriched.gzgc import load
load()
```

### Nyala Data

#### ::: reidhub.access.provenance.gzgc.download_and_extract 

<!--## Change above!!-->

Examples:

```python
from reidhub.access.enriched.nyala import load
load()
```


### Sea Star Re-ID 2023

#### ::: reidhub.access.provenance.gzgc.download_and_extract

Examples:

```python
from reidhub.access.enriched.seastars import load
load()
```
