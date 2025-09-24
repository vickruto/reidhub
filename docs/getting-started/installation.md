
`ReIDHub` requires **Python 3.9+** and works best inside a virtual environment ([poetry](https://python-poetry.org/) is highly recommended).


!!! note
    The project is still in its early stages of development and is not yet stable. Therefore there is no packaged release as of yet.  
    The recommended way to install is by cloning the repository and installing locally.


## Installing From Source

For now, the best way to install the reidhub package is by cloning the repo from Github and installing it 

You can install the repo locally using poetry as as shown below: 

```bash
# Clone the repository
git clone https://github.com/vickruto/reidhub.git

# Move into the project directory
cd reidhub

# Install the project & its dependencies with Poetry
poetry install
```

## Installing on Colab
Since Colab comes with pre-installed packages that may conflict with reidhub dependencies, it’s best to install only the required ones manually.

```bash
# input trunc/full commit hash if you want to load the code as of a particular commit
checkpoint_commit_hash = ""  

try:
    import reidhub 
    print('Loaded pre-installed package')

except:
    import os
    import sys
    !git clone https://github.com/vickruto/reidhub.git
    if checkpoint_commit_hash:
        !cd reidhub && git checkout {checkpoint_commit_hash}
    full_path = os.path.abspath('reidhub')
    sys.path.insert(0, full_path)
    print(f'added path {full_path} to sys.path')
    import reidhub
    print('\n\nSuccessfully cloned and loaded package from github')

!uv pip install fiftyone # install other packages manually
```

Here is an example of a Colab compatible notebook: [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/vickruto/reidhub/blob/main/notebooks/2025-09-22-reidhub-checkpoint.ipynb "Open this notebook in Colab")

