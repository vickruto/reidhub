# ReIDHub

*A central hub for open-source animal re-identification datasets, built on the Access–Assess–Address framework.*  

[![Tests](https://github.com/vickruto/reidhub/workflows/Test/badge.svg)](https://github.com/vickruto/reidhub/actions/workflows/test.yml)
[![Code Quality](https://github.com/vickruto/reidhub/workflows/Code%20Quality/badge.svg)](https://github.com/vickruto/reidhub/actions/workflows/code-quality.yml)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Poetry](https://img.shields.io/badge/poetry-1.0+-blue.svg)](https://python-poetry.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)


## Table of Contents
1. [Project Overview](#📌-project-overview)
2. [Features](#✨-features)
3. [Datasets](#🗂-datasets) 
4. [Documentation](#📖-documentation) 
5. [The Fynesse Framework](#fynesse-framework)
   - [Fynesse Paradigm Aspects](#fynesse-paradigm-aspects)
      - [Access](#1-access)
      - [Assess](#2-assess)
      - [Address](#3-address) 
6. [Setting Up](#setting-up)
    - [Prerequisites](#prerequisites)
    - [Clone this repository](#clone-this-repository)
    - [Installation](#installation)
    - [Development Workflow](#development-workflow)
      - [Adding dependencies](#adding-dependencies)
 <!-- 6. Acknowledgements-->


## 📌 Project Overview  

ReIDHub is a mini-project that centralizes open-source **animal re-identification (ReID) datasets** to make research more **reproducible, reusable, and accessible**.  
The project is greatly inspired by the [pods](https://github.com/sods/ods) project.   
It applies the [**Access–Assess–Address (AAA) framework**](https://inverseprobability.com/talks/notes/access-assess-address-a-pipeline-for-automated-data-science.html) to the data science workflow:  

- **Access** → Standardize dataset ingestion, caching, and visualization.  
- **Assess** → Profile datasets, run baselines, and benchmark models.  
- **Address** → Reuse curated datasets and precomputed outputs for downstream research.  

The goal is to reduce friction in re-identification workflows: no more repeated preprocessing, inconsistent dataset structures, or scattered benchmarks.  

## ✨ Features  

- 🔗 **Dataset registry** for open-source animal ReID datasets  
- 📂 **Standardized loaders** with cached splits, embeddings, predictions, captions etc 
- 👀 **FiftyOne integration** for easy dataset visualization  
- 📊 **Dataset profiling & baselines** (distribution stats, mAP, retrieval metrics)  
- 📑 **Benchmark tracker** linking datasets to research papers & published results  
- 📦 Portable, reproducible exports for reuse in new experiments  

## 🗂 Datasets  

ReIDHub will initially support multiple open-source datasets (with links and readiness states):  

- 🦓 **Great Zebra and Giraffe Count and ID** – [Lila Datasets Page](https://lila.science/datasets/great-zebra-giraffe-id)  
- 🦓 **Beluga ID 2022** – [Lila Datasets Page](https://lila.science/datasets/beluga-id-2022/)  
- 🦓 **Leopard ID 2022** – [Lila Datasets Page](https://lila.science/datasets/leopard-id-2022/)  
- 🦓 **Sea Star Re-ID 2023** – [Lila Datasets Page](https://lila.science/sea-star-re-id-2023/)  
- 🐘 **Hyena ID 2022** – [Lila Datasets Page](https://lila.science/datasets/hyena-id-2022/)  
- 🐋 **WhaleID / Happywhale** – [Kaggle link](https://www.kaggle.com/competitions/happy-whale-and-dolphin)  

Each dataset will include:  
- Download/ingestion instructions  
- Data readiness level (see [Data Readiness Levels](https://inverseprobability.com/publications/data-readiness-levels.html))  
- Dataset statistics and visualizations  
- Baseline benchmarks (local + literature)  


## 📖 Documentation  

- **Docs site (MkDocs)**: [Coming soon]  
- Each dataset will have a dedicated page with:  
  - Dataset description  
  - Static visualizations (ID distributions, maps etc)
  - Download instructions  
  - Benchmark summaries  
  - Publications summaries and links  

## 🚀 Roadmap  

- [*] Implement dataset registry (Access)  
- [ ] Add FiftyOne dataset conversion/export  
- [ ] Add profiling and baseline benchmarks (Assess)  
- [ ] Enable cached embeddings/predictions for reuse (Address)  
- [ ] Build MkDocs documentation site  
- [ ] Publish package to PyPI  


## Fynesse Framework
This is repository is built on the [Fynesse GitHub template repository](https://github.com/lawrennd/fynesse_template). The Fynesse framework is built for repeatabilitiy of data analysis projects. The template uses Poetry for dependency management, pytest for testing, and follows current Python development best practices.

You can refer to these sources to learn more about the Fynesse Framework:
 - [Github template repository README](https://github.com/lawrennd/fynesse_template/blob/main/README.md)
 - [Access, Assess and Address: A Pipeline for (Automated?) Data Science](https://inverseprobability.com/talks/notes/access-assess-address-a-pipeline-for-automated-data-science.html). Neil's talk at ECML Workshop on Automating Data Science on Sep 17, 2021 

The Fynesse paradigm is inspired by experience in operational data science both in the Amazon supply chain and in the UK Covid-19 pandemic response.

The Fynesse paradigm considers three aspects to data analysis, Access, Assess, Address.


### Fynesse Paradigm Aspects
The Fynesse paradigm considers three aspects to data analysis, `Access`, `Assess`, `Address`.

#### 1. Access
Ensuring you can obtain and legally use the data. This includes overcoming technical barriers (distributed systems, obscure APIs, digitization challenges) and legal barriers (IP rights, licensing, privacy). Proper access also requires documenting provenance and managing data ecosystems in a structured way.


#### 2. Assess
Understanding the nature and quality of the data before analysis. This involves checking for missing values, outliers, encodings, and overall reliability—without tailoring to a specific question. The goal is to make repeatable, context-agnostic assessments that others can reuse.


#### 3. Address
Applying the data to the actual question or problem. This may involve building predictive models, statistical analyses, or creating visualizations and dashboards. It’s the most familiar step to researchers, as it’s where insights are derived and communicated.


## Setting Up

### Prerequisites
- Python 3.9 or higher
- Poetry (install via `curl -sSL https://install.python-poetry.org | python3 -`)
- make  
If you are working in a UNIX based system (Linux or Mac) then you already have `make` installed. If you are working on Windows, you might have to install it. 

### Clone this repository

```bash
# Clone the repo
git clone https://github.com/vickruto/reidhub.git
cd reidhub
```


### Installation

<details open>
<summary>Option 1: Makefile</summary>

```bash
# Install dependencies & run tests to verify installation
make install & make test
```

</details> 


<details> 
<summary>Option 2: Ordinary Bash</summary>

```bash
# Install dependencies with Poetry
poetry install

# Activate the virtual environment
poetry shell

# Run tests to verify installation
poetry run pytest
```

</details>


### Development Workflow

<details open>
<summary>Option 1: Makefile</summary>

```bash
# Install core project dependencies
make install

# Install development dependencies
make dev

# Run tests
make test

# Format code
make format

# Type checking
make type-check

# Linting
make lint

# Run code quality checks (format + lint + type-check)
make quality

# Run full validation (tests + format + lint + type-check)
make check

# Clean cache and build artifacts
make clean
```
</details>

<details>
<summary>Option 2: Ordinary Bash</summary>

```bash
# Install development dependencies
poetry install --with dev

# Run tests
poetry run pytest

# Format code
poetry run black fynesse/

# Type checking
poetry run mypy fynesse/

# Linting
poetry run flake8 fynesse/
```
</details>


##### Adding Dependencies

```bash
# To add a dependency (eg pandas):
poetry add pandas

or 

poetry add pandas --group dev # If you only need it for development
```

The commands above will update the `pyproject.toml` with the latest version of the dependency requested that does not cause a dependency conflict with the already added dependencies. It also automatically updates the lockfile `poetry.lock` ensuring that the analysis is reproducible in any system. 
