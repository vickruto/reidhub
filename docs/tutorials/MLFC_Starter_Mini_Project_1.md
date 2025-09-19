## Access


### todos:
1) Download the following datasets

2) Unzip them and format them in YOLO/Fiftyone format

## Types of Data Sources:
1. Github
2. Zip downloads
3. Kaggle
4. Hugging Face


```python
!apt install -y tree &> /dev/null
```


```python
!pip install yamllint
```

    Collecting yamllint
      Downloading yamllint-1.37.1-py3-none-any.whl.metadata (4.3 kB)
    Collecting pathspec>=0.5.3 (from yamllint)
      Downloading pathspec-0.12.1-py3-none-any.whl.metadata (21 kB)
    Requirement already satisfied: pyyaml in /usr/local/lib/python3.12/dist-packages (from yamllint) (6.0.2)
    Downloading yamllint-1.37.1-py3-none-any.whl (68 kB)
    [?25l   [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m0.0/68.8 kB[0m [31m?[0m eta [36m-:--:--[0m[2K   [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m68.8/68.8 kB[0m [31m3.3 MB/s[0m eta [36m0:00:00[0m
    [?25hDownloading pathspec-0.12.1-py3-none-any.whl (31 kB)
    Installing collected packages: pathspec, yamllint
    Successfully installed pathspec-0.12.1 yamllint-1.37.1



```python
%%writefile datasets2.yaml
####################################################################################
### DATASETS
### This file contains information and metadata for each dataset
####################################################################################

gzgc:
    url:
        - https://storage.googleapis.com/public-datasets-lila/wild-me/gzgc.coco.tar.gz  ## GCP LINK
    size: 10240
    species:
        - zebra
        - giraffe
    citations:
        - |
          @inproceedings{parham2017animal,
            title={Animal population censusing at scale with citizen science and photographic identification},
            author={Parham, Jason and Crall, Jonathan and Stewart, Charles and Berger-Wolf, Tanya and Rubenstein, Daniel I},
            booktitle={AAAI spring symposium-technical report},
            year={2017}
          }
        -

hyena_id_2022:
    url:
        - https://storage.googleapis.com/public-datasets-lila/wild-me/hyena.coco.tar.gz  ## GCP LINK
    size: 3072
    species:
        - hyena
    citations:
        - |
          Botswana Predator Conservation Trust (2022). Panthera pardus CSV custom export. Retrieved from African Carnivore Wildbook 2022-04-28.
        -

leopard_id_2022:
    url:
        - https://storage.googleapis.com/public-datasets-lila/wild-me/leopard.coco.tar.gz  ## GCP LINK
    size: 8192
    species:
        - leopard
    citations:
        - |
          Botswana Predator Conservation Trust (2022). Panthera pardus CSV custom export. Retrieved from African Carnivore Wildbook 2022-04-28.
        -


beluga_id_2022:
    url:
        - https://storage.googleapis.com/public-datasets-lila/wild-me/beluga.coco.tar.gz  ## train split
        - https://storage.googleapis.com/public-datasets-lila/wild-me/beluga-id-test.zip  ## test split
    size: 680
    species:
        - beluga whale
    citations:
        -
        -

nyala_data:
    url:
        - https://github.com/tvanzyl/wildlife_reidentification/tree/main/Nyala_Data_Zero  ## Github
    size:
    species:
        - nyala
    citations:
        -
        -

sea_star_reid:
    url:
        - https://storage.googleapis.com/public-datasets-lila/sea-star-re-id/sea-star-re-id.zip  ## Github
    size:
    species:
        - sea star
    citations:
        - |
          @article{wahltinez2024open,
            title={An open-source general purpose machine learning framework for individual animal re-identification using few-shot learning},
            author={Wahltinez, Oscar and Wahltinez, Sarah J},
            journal={Methods in Ecology and Evolution},
            volume={15},
            number={2},
            pages={373--387},
            year={2024},
            publisher={Wiley Online Library}
            }
        -

```

    Overwriting datasets2.yaml



```python
%%writefile .yamllint
extends: default

rules:
  line-length:
    max: 120
    level: warning
  indentation:
    spaces: 2
    indent-sequences: true
  truthy:
    check-keys: false
```

    Writing .yamllint



```python
import yaml

config_path = 'datasets2.yaml'

with open(config_path, 'r') as f:
    CONFIG = yaml.safe_load(f)

print(CONFIG)
```

    {'gzgc': {'url': ['https://storage.googleapis.com/public-datasets-lila/wild-me/gzgc.coco.tar.gz'], 'size': 10240, 'species': ['zebra', 'giraffe'], 'citations': ['@inproceedings{parham2017animal,\n  title={Animal population censusing at scale with citizen science and photographic identification},\n  author={Parham, Jason and Crall, Jonathan and Stewart, Charles and Berger-Wolf, Tanya and Rubenstein, Daniel I},\n  booktitle={AAAI spring symposium-technical report},\n  year={2017}\n}\n', None]}, 'hyena_id_2022': {'url': ['https://storage.googleapis.com/public-datasets-lila/wild-me/hyena.coco.tar.gz'], 'size': 3072, 'species': ['hyena'], 'citations': ['Botswana Predator Conservation Trust (2022). Panthera pardus CSV custom export. Retrieved from African Carnivore Wildbook 2022-04-28.\n', None]}, 'leopard_id_2022': {'url': ['https://storage.googleapis.com/public-datasets-lila/wild-me/leopard.coco.tar.gz'], 'size': 8192, 'species': ['leopard'], 'citations': ['Botswana Predator Conservation Trust (2022). Panthera pardus CSV custom export. Retrieved from African Carnivore Wildbook 2022-04-28.\n', None]}, 'beluga_id_2022': {'url': ['https://storage.googleapis.com/public-datasets-lila/wild-me/beluga.coco.tar.gz', 'https://storage.googleapis.com/public-datasets-lila/wild-me/beluga-id-test.zip'], 'size': 680, 'species': ['beluga whale'], 'citations': [None, None]}, 'nyala_data': {'url': ['https://github.com/tvanzyl/wildlife_reidentification/tree/main/Nyala_Data_Zero'], 'size': None, 'species': ['nyala'], 'citations': [None, None]}, 'sea_star_reid': {'url': ['https://storage.googleapis.com/public-datasets-lila/sea-star-re-id/sea-star-re-id.zip'], 'size': None, 'species': ['sea star'], 'citations': ['@article{wahltinez2024open,\n  title={An open-source general purpose machine learning framework for individual animal re-identification using few-shot learning},\n  author={Wahltinez, Oscar and Wahltinez, Sarah J},\n  journal={Methods in Ecology and Evolution},\n  volume={15},\n  number={2},\n  pages={373--387},\n  year={2024},\n  publisher={Wiley Online Library}\n  }\n', None]}}



```python
!yamllint -c .yamllint datasets2.yaml
```

    [4mdatasets2.yaml[0m
      [2m2:13[0m      [31merror[0m    trailing spaces  [2m(trailing-spaces)[0m
      [2m6:1[0m       [33mwarning[0m  missing document start "---"  [2m(document-start)[0m
      [2m7:5[0m       [31merror[0m    wrong indentation: expected 2 but found 4  [2m(indentation)[0m
      [2m8:9[0m       [31merror[0m    wrong indentation: expected 6 but found 8  [2m(indentation)[0m
      [2m10:13[0m     [31merror[0m    trailing spaces  [2m(trailing-spaces)[0m
      [2m11:9[0m      [31merror[0m    wrong indentation: expected 6 but found 8  [2m(indentation)[0m
      [2m13:15[0m     [31merror[0m    trailing spaces  [2m(trailing-spaces)[0m
      [2m14:9[0m      [31merror[0m    wrong indentation: expected 6 but found 8  [2m(indentation)[0m
      [2m17:121[0m    [33mwarning[0m  line too long (124 > 120 characters)  [2m(line-length)[0m
      [2m21:10[0m     [31merror[0m    trailing spaces  [2m(trailing-spaces)[0m
      [2m24:5[0m      [31merror[0m    wrong indentation: expected 2 but found 4  [2m(indentation)[0m
      [2m24:9[0m      [31merror[0m    trailing spaces  [2m(trailing-spaces)[0m
      [2m25:9[0m      [31merror[0m    wrong indentation: expected 6 but found 8  [2m(indentation)[0m
      [2m27:13[0m     [31merror[0m    trailing spaces  [2m(trailing-spaces)[0m
      [2m28:9[0m      [31merror[0m    wrong indentation: expected 6 but found 8  [2m(indentation)[0m
      [2m29:15[0m     [31merror[0m    trailing spaces  [2m(trailing-spaces)[0m
      [2m30:9[0m      [31merror[0m    wrong indentation: expected 6 but found 8  [2m(indentation)[0m
      [2m31:121[0m    [33mwarning[0m  line too long (143 > 120 characters)  [2m(line-length)[0m
      [2m32:10[0m     [31merror[0m    trailing spaces  [2m(trailing-spaces)[0m
      [2m33:1[0m      [31merror[0m    trailing spaces  [2m(trailing-spaces)[0m
      [2m35:5[0m      [31merror[0m    wrong indentation: expected 2 but found 4  [2m(indentation)[0m
      [2m35:9[0m      [31merror[0m    trailing spaces  [2m(trailing-spaces)[0m
      [2m36:9[0m      [31merror[0m    wrong indentation: expected 6 but found 8  [2m(indentation)[0m
      [2m38:13[0m     [31merror[0m    trailing spaces  [2m(trailing-spaces)[0m
      [2m39:9[0m      [31merror[0m    wrong indentation: expected 6 but found 8  [2m(indentation)[0m
      [2m40:15[0m     [31merror[0m    trailing spaces  [2m(trailing-spaces)[0m
      [2m41:9[0m      [31merror[0m    wrong indentation: expected 6 but found 8  [2m(indentation)[0m
      [2m42:121[0m    [33mwarning[0m  line too long (143 > 120 characters)  [2m(line-length)[0m
      [2m43:10[0m     [31merror[0m    trailing spaces  [2m(trailing-spaces)[0m
      [2m44:1[0m      [31merror[0m    trailing spaces  [2m(trailing-spaces)[0m
      [2m47:5[0m      [31merror[0m    wrong indentation: expected 2 but found 4  [2m(indentation)[0m
      [2m47:9[0m      [31merror[0m    trailing spaces  [2m(trailing-spaces)[0m
      [2m48:9[0m      [31merror[0m    wrong indentation: expected 6 but found 8  [2m(indentation)[0m
      [2m51:13[0m     [31merror[0m    trailing spaces  [2m(trailing-spaces)[0m
      [2m52:9[0m      [31merror[0m    wrong indentation: expected 6 but found 8  [2m(indentation)[0m
      [2m53:15[0m     [31merror[0m    trailing spaces  [2m(trailing-spaces)[0m
      [2m54:9[0m      [31merror[0m    wrong indentation: expected 6 but found 8  [2m(indentation)[0m
      [2m54:10[0m     [31merror[0m    trailing spaces  [2m(trailing-spaces)[0m
      [2m55:10[0m     [31merror[0m    trailing spaces  [2m(trailing-spaces)[0m
      [2m56:1[0m      [31merror[0m    trailing spaces  [2m(trailing-spaces)[0m
      [2m58:5[0m      [31merror[0m    wrong indentation: expected 2 but found 4  [2m(indentation)[0m
      [2m58:9[0m      [31merror[0m    trailing spaces  [2m(trailing-spaces)[0m
      [2m59:9[0m      [31merror[0m    wrong indentation: expected 6 but found 8  [2m(indentation)[0m
      [2m60:10[0m     [31merror[0m    trailing spaces  [2m(trailing-spaces)[0m
      [2m61:13[0m     [31merror[0m    trailing spaces  [2m(trailing-spaces)[0m
      [2m62:9[0m      [31merror[0m    wrong indentation: expected 6 but found 8  [2m(indentation)[0m
      [2m63:15[0m     [31merror[0m    trailing spaces  [2m(trailing-spaces)[0m
      [2m64:9[0m      [31merror[0m    wrong indentation: expected 6 but found 8  [2m(indentation)[0m
      [2m64:10[0m     [31merror[0m    trailing spaces  [2m(trailing-spaces)[0m
      [2m65:10[0m     [31merror[0m    trailing spaces  [2m(trailing-spaces)[0m
      [2m66:1[0m      [31merror[0m    trailing spaces  [2m(trailing-spaces)[0m
      [2m68:5[0m      [31merror[0m    wrong indentation: expected 2 but found 4  [2m(indentation)[0m
      [2m68:9[0m      [31merror[0m    trailing spaces  [2m(trailing-spaces)[0m
      [2m69:9[0m      [31merror[0m    wrong indentation: expected 6 but found 8  [2m(indentation)[0m
      [2m70:10[0m     [31merror[0m    trailing spaces  [2m(trailing-spaces)[0m
      [2m71:13[0m     [31merror[0m    trailing spaces  [2m(trailing-spaces)[0m
      [2m72:9[0m      [31merror[0m    wrong indentation: expected 6 but found 8  [2m(indentation)[0m
      [2m73:15[0m     [31merror[0m    trailing spaces  [2m(trailing-spaces)[0m
      [2m74:9[0m      [31merror[0m    wrong indentation: expected 6 but found 8  [2m(indentation)[0m
      [2m76:121[0m    [33mwarning[0m  line too long (142 > 120 characters)  [2m(line-length)[0m
      [2m85:10[0m     [31merror[0m    trailing spaces  [2m(trailing-spaces)[0m
    



```python
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,  # logging levels: (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    format='%(asctime)s - %(levelname)s - %(message)s',  # Log format
    handlers=[
        logging.FileHandler('access.log'),  # Log to a file
        logging.StreamHandler()  # Also output to console
    ]
)
```


```python
import subprocess
import os
import logging

def download_and_extract_gzgc(config):
    url = config['url'][0]
    filename = url.split('/')[-1]

    # Download the file
    if not os.path.exists(filename):
        logging.info(f"Downloading {filename}...")
        subprocess.run(["wget", url], check=True)
    else:
        logging.info(f"{filename} already exists. Skipping download.")

    # Extract the file
    if os.path.exists(filename):
        logging.info(f"Extracting {filename}...")
        subprocess.run(["tar", "-xf", filename], check=True)
        logging.info("Extraction complete.")
    else:
        logging.error(f"Error: {filename} not found for extraction.")

download_and_extract_gzgc(CONFIG['gzgc'])
```


```python
## Rewrite the function but in a way that it does not rely on apt packages
## Refactor it later to do the following:
## 1) use a reidhub cache folder
## 2) remove the zip/tar file after downloading and unzipping successfully

import os
import logging
import requests
import tarfile

def download_and_extract_gzgc(config):
    url = config['url'][0]
    filename = url.split('/')[-1]

    # Download the file
    if not os.path.exists(filename):
        logging.info(f"Downloading {filename}...")
        try:
            response = requests.get(url, stream=True)
            response.raise_for_status()  # Will raise an exception for HTTP errors
            with open(filename, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
            logging.info(f"Download complete: {filename}")
        except requests.exceptions.RequestException as e:
            logging.error(f"Error downloading {filename}: {e}")
            return
    else:
        logging.info(f"{filename} already exists. Skipping download.")

    # Extract the file
    if os.path.exists(filename):
        logging.info(f"Extracting {filename}...")
        try:
            with tarfile.open(filename, 'r:gz') as tar:
                tar.extractall()  # You can specify a path in extractall() if you need
            logging.info("Extraction complete.")
        except tarfile.TarError as e:
            logging.error(f"Error extracting {filename}: {e}")
    else:
        logging.error(f"Error: {filename} not found for extraction.")

```


```python
CONFIG['gzgc']['url'][0]
```




    'https://storage.googleapis.com/public-datasets-lila/wild-me/gzgc.coco.tar.gz'




```python

```


```python

```


```python

```


```python
# !svn export https://github.com/tvanzyl/wildlife_reidentification/tree/main/Nyala_Data_Zero Nyala_Data_Zero
```


```python
!mkdir -p access/download
!touch access/download/nyala.py
```


```python
%%writefile access/download/nyala.py
import os
import subprocess

# Define the repository URL and the subdirectory path
repo_url = "https://github.com/tvanzyl/wildlife_reidentification.git"
subdirectory_path = "Nyala_Data_Zero"
local_dir = "Nyala_Data_Zero"

# Clone the repository with sparse-checkout enabled
if not os.path.exists(".git"):
    subprocess.run(["git", "init"], check=True)
    subprocess.run(["git", "remote", "add", "-f", "origin", repo_url], check=True)
    subprocess.run(["git", "config", "core.sparseCheckout", "true"], check=True)

# Define the sparse-checkout patterns
with open(".git/info/sparse-checkout", "w") as f:
    f.write(f"{subdirectory_path}\n")

# Pull only the specified subdirectory
subprocess.run(["git", "pull", "origin", "main"], check=True)

# Move the subdirectory to the desired location
# Note: git sparse-checkout will place the subdirectory at the root of the cloned repo,
# so we need to move it.
if os.path.exists(subdirectory_path):
    os.rename(subdirectory_path, local_dir)
    print(f"Successfully downloaded '{subdirectory_path}' to '{local_dir}'")
else:
    print(f"Error: Subdirectory '{subdirectory_path}' not found after sparse checkout.")
```

    Overwriting access/download/nyala.py



```python
!tree Nyala_Data_Zero
```


```python

```

## Assess


```python
!uv pip install fiftyone # &> /dev/null
```

    [2mUsing Python 3.12.11 environment at: /usr[0m
    [2K[2mResolved [1m109 packages[0m [2min 78ms[0m[0m
    [2K[2mPrepared [1m1 package[0m [2min 713ms[0m[0m
    [2mUninstalled [1m2 packages[0m [2min 1.41s[0m[0m
    [2K[2mInstalled [1m44 packages[0m [2min 209ms[0m[0m
     [32m+[39m [1margcomplete[0m[2m==3.6.2[0m
     [32m+[39m [1masync-lru[0m[2m==2.0.5[0m
     [32m+[39m [1mbcrypt[0m[2m==4.3.0[0m
     [32m+[39m [1mboto3[0m[2m==1.40.32[0m
     [32m+[39m [1mbotocore[0m[2m==1.40.32[0m
     [32m+[39m [1mdacite[0m[2m==1.9.2[0m
     [32m+[39m [1mdeprecated[0m[2m==1.2.18[0m
     [32m+[39m [1mdnspython[0m[2m==2.8.0[0m
     [32m+[39m [1mfiftyone[0m[2m==1.8.0[0m
     [32m+[39m [1mfiftyone-brain[0m[2m==0.21.3[0m
     [32m+[39m [1mfiftyone-db[0m[2m==1.3.0[0m
     [32m+[39m [1mftfy[0m[2m==6.3.1[0m
     [32m+[39m [1mgraphql-core[0m[2m==3.2.6[0m
     [32m+[39m [1mhypercorn[0m[2m==0.17.3[0m
     [32m+[39m [1minflate64[0m[2m==1.0.3[0m
     [32m+[39m [1mjmespath[0m[2m==1.0.1[0m
     [32m+[39m [1mjsonlines[0m[2m==4.0.0[0m
     [32m+[39m [1mlia-web[0m[2m==0.2.3[0m
     [32m+[39m [1mmongoengine[0m[2m==0.29.1[0m
     [32m+[39m [1mmotor[0m[2m==3.6.1[0m
     [32m+[39m [1mmultivolumefile[0m[2m==0.2.3[0m
     [32m+[39m [1mparamiko[0m[2m==3.5.1[0m
     [31m-[39m [1mplotly[0m[2m==5.24.1[0m
     [32m+[39m [1mplotly[0m[2m==6.3.0[0m
     [32m+[39m [1mpprintpp[0m[2m==0.4.0[0m
     [32m+[39m [1mpriority[0m[2m==2.0.0[0m
     [32m+[39m [1mpy7zr[0m[2m==1.0.0[0m
     [32m+[39m [1mpybcj[0m[2m==1.0.6[0m
     [32m+[39m [1mpydash[0m[2m==8.0.5[0m
     [32m+[39m [1mpymongo[0m[2m==4.9.2[0m
     [32m+[39m [1mpynacl[0m[2m==1.6.0[0m
     [32m+[39m [1mpyppmd[0m[2m==1.2.0[0m
     [32m+[39m [1mpyzstd[0m[2m==0.17.0[0m
     [32m+[39m [1mrarfile[0m[2m==4.2[0m
     [32m+[39m [1mretrying[0m[2m==1.4.2[0m
     [32m+[39m [1mrtree[0m[2m==1.4.1[0m
     [32m+[39m [1ms3transfer[0m[2m==0.14.0[0m
     [31m-[39m [1msse-starlette[0m[2m==3.0.2[0m
     [32m+[39m [1msse-starlette[0m[2m==0.10.3[0m
     [32m+[39m [1msseclient-py[0m[2m==1.8.0[0m
     [32m+[39m [1mstrawberry-graphql[0m[2m==0.282.0[0m
     [32m+[39m [1mtexttable[0m[2m==1.7.0[0m
     [32m+[39m [1muniversal-analytics-python3[0m[2m==1.1.1[0m
     [32m+[39m [1mvoxel51-eta[0m[2m==0.15.1[0m
     [32m+[39m [1mwsproto[0m[2m==1.2.0[0m
     [32m+[39m [1mxmltodict[0m[2m==1.0.1[0m



```python
from pathlib import Path
image_paths = Path('gzgc.coco/images').rglob('**/*.jpg')
image_paths = list(image_paths)
print(f'Found {len(image_paths)} images')

```

    Found 4948 images



```python
for img_path in image_paths[:4]:
    print(img_path)

```

    gzgc.coco/images/train2020/000000002284.jpg
    gzgc.coco/images/train2020/000000004822.jpg
    gzgc.coco/images/train2020/000000000540.jpg
    gzgc.coco/images/train2020/000000004938.jpg



```python
import json

annotation_file = '/content/gzgc.coco/annotations/instances_train2020.json'

with open(annotation_file, 'r') as f:
    annotations = json.load(f)

print(annotations.keys())
```

    dict_keys(['info', 'licenses', 'categories', 'images', 'annotations', 'parts'])



```python
import pandas as pd
images_df = pd.DataFrame(annotations['images'])
images_df
```





  <div id="df-564145bb-f627-4888-b1f1-c39a6fd00f09" class="colab-df-container">
    <div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>license</th>
      <th>file_name</th>
      <th>photographer</th>
      <th>coco_url</th>
      <th>height</th>
      <th>width</th>
      <th>date_captured</th>
      <th>gps_lat_captured</th>
      <th>gps_lon_captured</th>
      <th>flickr_url</th>
      <th>id</th>
      <th>uuid</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>3</td>
      <td>000000000001.jpg</td>
      <td>NNP GZC Car '10WHITE', Person 'A', Image 0005</td>
      <td>None</td>
      <td>2000</td>
      <td>3000</td>
      <td>2015-03-01 14:53:46</td>
      <td>-1.351341</td>
      <td>36.800374</td>
      <td>None</td>
      <td>1</td>
      <td>826fb775-2f99-a8cf-7120-cba60562e82f</td>
    </tr>
    <tr>
      <th>1</th>
      <td>3</td>
      <td>000000000002.jpg</td>
      <td>NNP GZC Car '10WHITE', Person 'A', Image 0006</td>
      <td>None</td>
      <td>2000</td>
      <td>3000</td>
      <td>2015-03-01 14:53:46</td>
      <td>-1.351341</td>
      <td>36.800374</td>
      <td>None</td>
      <td>2</td>
      <td>26a32203-4923-723c-d1fb-d0e781010ee9</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>000000000003.jpg</td>
      <td>NNP GZC Car '10WHITE', Person 'A', Image 0007</td>
      <td>None</td>
      <td>2000</td>
      <td>3000</td>
      <td>2015-03-01 14:53:52</td>
      <td>-1.351341</td>
      <td>36.800374</td>
      <td>None</td>
      <td>3</td>
      <td>a35e6b20-1cc5-c958-8e11-d46065e9062d</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>000000000004.jpg</td>
      <td>NNP GZC Car '10WHITE', Person 'A', Image 0008</td>
      <td>None</td>
      <td>2000</td>
      <td>3000</td>
      <td>2015-03-01 14:53:58</td>
      <td>-1.351341</td>
      <td>36.800374</td>
      <td>None</td>
      <td>4</td>
      <td>5f369ecf-b1ac-eae3-4b23-e386786672b9</td>
    </tr>
    <tr>
      <th>4</th>
      <td>3</td>
      <td>000000000005.jpg</td>
      <td>NNP GZC Car '10WHITE', Person 'A', Image 0010</td>
      <td>None</td>
      <td>2000</td>
      <td>3000</td>
      <td>2015-03-01 15:02:32</td>
      <td>-1.367088</td>
      <td>36.781978</td>
      <td>None</td>
      <td>5</td>
      <td>981d8673-6440-3c95-2769-d1207033ffd0</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>4943</th>
      <td>3</td>
      <td>000000004944.jpg</td>
      <td></td>
      <td>None</td>
      <td>2000</td>
      <td>3000</td>
      <td>2015-02-26 13:50:34</td>
      <td>-1.376729</td>
      <td>36.830786</td>
      <td>None</td>
      <td>4944</td>
      <td>bdffb4cb-80c4-735e-f315-5398e3b94d7b</td>
    </tr>
    <tr>
      <th>4944</th>
      <td>3</td>
      <td>000000004945.jpg</td>
      <td></td>
      <td>None</td>
      <td>2000</td>
      <td>3000</td>
      <td>2015-02-26 13:50:40</td>
      <td>-1.370916</td>
      <td>36.791815</td>
      <td>None</td>
      <td>4945</td>
      <td>4aae3cb0-4798-90be-8933-15833fb6f969</td>
    </tr>
    <tr>
      <th>4945</th>
      <td>3</td>
      <td>000000004946.jpg</td>
      <td></td>
      <td>None</td>
      <td>2000</td>
      <td>3000</td>
      <td>2015-02-26 13:50:50</td>
      <td>-1.370916</td>
      <td>36.791815</td>
      <td>None</td>
      <td>4946</td>
      <td>db345e6d-742e-b5b6-9d84-c63fea9c2224</td>
    </tr>
    <tr>
      <th>4946</th>
      <td>3</td>
      <td>000000004947.jpg</td>
      <td></td>
      <td>None</td>
      <td>2000</td>
      <td>3000</td>
      <td>2015-02-26 13:51:10</td>
      <td>-1.370916</td>
      <td>36.791815</td>
      <td>None</td>
      <td>4947</td>
      <td>ca62a7b9-ea78-1f0d-48c4-6f8a4464489e</td>
    </tr>
    <tr>
      <th>4947</th>
      <td>3</td>
      <td>000000004948.jpg</td>
      <td></td>
      <td>None</td>
      <td>2000</td>
      <td>3000</td>
      <td>2015-02-26 13:51:17</td>
      <td>-1.370916</td>
      <td>36.791815</td>
      <td>None</td>
      <td>4948</td>
      <td>71577035-2041-b115-40c5-869a0fbcbdeb</td>
    </tr>
  </tbody>
</table>
<p>4948 rows × 12 columns</p>
</div>
    <div class="colab-df-buttons">

  <div class="colab-df-container">
    <button class="colab-df-convert" onclick="convertToInteractive('df-564145bb-f627-4888-b1f1-c39a6fd00f09')"
            title="Convert this dataframe to an interactive table."
            style="display:none;">

  <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960">
    <path d="M120-120v-720h720v720H120Zm60-500h600v-160H180v160Zm220 220h160v-160H400v160Zm0 220h160v-160H400v160ZM180-400h160v-160H180v160Zm440 0h160v-160H620v160ZM180-180h160v-160H180v160Zm440 0h160v-160H620v160Z"/>
  </svg>
    </button>

  <style>
    .colab-df-container {
      display:flex;
      gap: 12px;
    }

    .colab-df-convert {
      background-color: #E8F0FE;
      border: none;
      border-radius: 50%;
      cursor: pointer;
      display: none;
      fill: #1967D2;
      height: 32px;
      padding: 0 0 0 0;
      width: 32px;
    }

    .colab-df-convert:hover {
      background-color: #E2EBFA;
      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);
      fill: #174EA6;
    }

    .colab-df-buttons div {
      margin-bottom: 4px;
    }

    [theme=dark] .colab-df-convert {
      background-color: #3B4455;
      fill: #D2E3FC;
    }

    [theme=dark] .colab-df-convert:hover {
      background-color: #434B5C;
      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);
      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));
      fill: #FFFFFF;
    }
  </style>

    <script>
      const buttonEl =
        document.querySelector('#df-564145bb-f627-4888-b1f1-c39a6fd00f09 button.colab-df-convert');
      buttonEl.style.display =
        google.colab.kernel.accessAllowed ? 'block' : 'none';

      async function convertToInteractive(key) {
        const element = document.querySelector('#df-564145bb-f627-4888-b1f1-c39a6fd00f09');
        const dataTable =
          await google.colab.kernel.invokeFunction('convertToInteractive',
                                                    [key], {});
        if (!dataTable) return;

        const docLinkHtml = 'Like what you see? Visit the ' +
          '<a target="_blank" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'
          + ' to learn more about interactive tables.';
        element.innerHTML = '';
        dataTable['output_type'] = 'display_data';
        await google.colab.output.renderOutput(dataTable, element);
        const docLink = document.createElement('div');
        docLink.innerHTML = docLinkHtml;
        element.appendChild(docLink);
      }
    </script>
  </div>


    <div id="df-a388c50f-6877-453a-bd90-64a6532851f2">
      <button class="colab-df-quickchart" onclick="quickchart('df-a388c50f-6877-453a-bd90-64a6532851f2')"
                title="Suggest charts"
                style="display:none;">

<svg xmlns="http://www.w3.org/2000/svg" height="24px"viewBox="0 0 24 24"
     width="24px">
    <g>
        <path d="M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zM9 17H7v-7h2v7zm4 0h-2V7h2v10zm4 0h-2v-4h2v4z"/>
    </g>
</svg>
      </button>

<style>
  .colab-df-quickchart {
      --bg-color: #E8F0FE;
      --fill-color: #1967D2;
      --hover-bg-color: #E2EBFA;
      --hover-fill-color: #174EA6;
      --disabled-fill-color: #AAA;
      --disabled-bg-color: #DDD;
  }

  [theme=dark] .colab-df-quickchart {
      --bg-color: #3B4455;
      --fill-color: #D2E3FC;
      --hover-bg-color: #434B5C;
      --hover-fill-color: #FFFFFF;
      --disabled-bg-color: #3B4455;
      --disabled-fill-color: #666;
  }

  .colab-df-quickchart {
    background-color: var(--bg-color);
    border: none;
    border-radius: 50%;
    cursor: pointer;
    display: none;
    fill: var(--fill-color);
    height: 32px;
    padding: 0;
    width: 32px;
  }

  .colab-df-quickchart:hover {
    background-color: var(--hover-bg-color);
    box-shadow: 0 1px 2px rgba(60, 64, 67, 0.3), 0 1px 3px 1px rgba(60, 64, 67, 0.15);
    fill: var(--button-hover-fill-color);
  }

  .colab-df-quickchart-complete:disabled,
  .colab-df-quickchart-complete:disabled:hover {
    background-color: var(--disabled-bg-color);
    fill: var(--disabled-fill-color);
    box-shadow: none;
  }

  .colab-df-spinner {
    border: 2px solid var(--fill-color);
    border-color: transparent;
    border-bottom-color: var(--fill-color);
    animation:
      spin 1s steps(1) infinite;
  }

  @keyframes spin {
    0% {
      border-color: transparent;
      border-bottom-color: var(--fill-color);
      border-left-color: var(--fill-color);
    }
    20% {
      border-color: transparent;
      border-left-color: var(--fill-color);
      border-top-color: var(--fill-color);
    }
    30% {
      border-color: transparent;
      border-left-color: var(--fill-color);
      border-top-color: var(--fill-color);
      border-right-color: var(--fill-color);
    }
    40% {
      border-color: transparent;
      border-right-color: var(--fill-color);
      border-top-color: var(--fill-color);
    }
    60% {
      border-color: transparent;
      border-right-color: var(--fill-color);
    }
    80% {
      border-color: transparent;
      border-right-color: var(--fill-color);
      border-bottom-color: var(--fill-color);
    }
    90% {
      border-color: transparent;
      border-bottom-color: var(--fill-color);
    }
  }
</style>

      <script>
        async function quickchart(key) {
          const quickchartButtonEl =
            document.querySelector('#' + key + ' button');
          quickchartButtonEl.disabled = true;  // To prevent multiple clicks.
          quickchartButtonEl.classList.add('colab-df-spinner');
          try {
            const charts = await google.colab.kernel.invokeFunction(
                'suggestCharts', [key], {});
          } catch (error) {
            console.error('Error during call to suggestCharts:', error);
          }
          quickchartButtonEl.classList.remove('colab-df-spinner');
          quickchartButtonEl.classList.add('colab-df-quickchart-complete');
        }
        (() => {
          let quickchartButtonEl =
            document.querySelector('#df-a388c50f-6877-453a-bd90-64a6532851f2 button');
          quickchartButtonEl.style.display =
            google.colab.kernel.accessAllowed ? 'block' : 'none';
        })();
      </script>
    </div>

  <div id="id_461489e7-4d9d-450a-bc87-84d2a2f3d3a2">
    <style>
      .colab-df-generate {
        background-color: #E8F0FE;
        border: none;
        border-radius: 50%;
        cursor: pointer;
        display: none;
        fill: #1967D2;
        height: 32px;
        padding: 0 0 0 0;
        width: 32px;
      }

      .colab-df-generate:hover {
        background-color: #E2EBFA;
        box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);
        fill: #174EA6;
      }

      [theme=dark] .colab-df-generate {
        background-color: #3B4455;
        fill: #D2E3FC;
      }

      [theme=dark] .colab-df-generate:hover {
        background-color: #434B5C;
        box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);
        filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));
        fill: #FFFFFF;
      }
    </style>
    <button class="colab-df-generate" onclick="generateWithVariable('images_df')"
            title="Generate code using this dataframe."
            style="display:none;">

  <svg xmlns="http://www.w3.org/2000/svg" height="24px"viewBox="0 0 24 24"
       width="24px">
    <path d="M7,19H8.4L18.45,9,17,7.55,7,17.6ZM5,21V16.75L18.45,3.32a2,2,0,0,1,2.83,0l1.4,1.43a1.91,1.91,0,0,1,.58,1.4,1.91,1.91,0,0,1-.58,1.4L9.25,21ZM18.45,9,17,7.55Zm-12,3A5.31,5.31,0,0,0,4.9,8.1,5.31,5.31,0,0,0,1,6.5,5.31,5.31,0,0,0,4.9,4.9,5.31,5.31,0,0,0,6.5,1,5.31,5.31,0,0,0,8.1,4.9,5.31,5.31,0,0,0,12,6.5,5.46,5.46,0,0,0,6.5,12Z"/>
  </svg>
    </button>
    <script>
      (() => {
      const buttonEl =
        document.querySelector('#id_461489e7-4d9d-450a-bc87-84d2a2f3d3a2 button.colab-df-generate');
      buttonEl.style.display =
        google.colab.kernel.accessAllowed ? 'block' : 'none';

      buttonEl.onclick = () => {
        google.colab.notebook.generateWithVariable('images_df');
      }
      })();
    </script>
  </div>

    </div>
  </div>





```python
import pandas as pd
annots_df = pd.DataFrame(annotations['annotations'])
annots_df
```





  <div id="df-92735753-2e56-4e20-aff9-d2785ae468da" class="colab-df-container">
    <div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>bbox</th>
      <th>theta</th>
      <th>viewpoint</th>
      <th>segmentation</th>
      <th>segmentation_bbox</th>
      <th>area</th>
      <th>iscrowd</th>
      <th>id</th>
      <th>image_id</th>
      <th>category_id</th>
      <th>uuid</th>
      <th>individual_ids</th>
      <th>isinterest</th>
      <th>name</th>
      <th>review_ids</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>[895.5, 437.0, 1221.0, 690.0]</td>
      <td>0.0</td>
      <td>left</td>
      <td>[[896, 437, 2116, 437, 2116, 1127, 896, 1127, ...</td>
      <td>[896, 437, 1220, 690]</td>
      <td>841800</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>7cfac6bc-379a-4859-a5c8-b21b06d2fe3d</td>
      <td>[2, 1, 3, 3459]</td>
      <td>0</td>
      <td>IBEIS_PZ_1561</td>
      <td>[]</td>
    </tr>
    <tr>
      <th>1</th>
      <td>[951.0, 488.5, 1178.5, 728.5]</td>
      <td>0.0</td>
      <td>left</td>
      <td>[[951, 488, 2130, 488, 2130, 1217, 951, 1217, ...</td>
      <td>[951, 488, 1179, 729]</td>
      <td>859491</td>
      <td>0</td>
      <td>2</td>
      <td>2</td>
      <td>1</td>
      <td>f56434d5-d829-4b56-a511-6e6c91b2f4fd</td>
      <td>[2, 1, 3, 3459]</td>
      <td>0</td>
      <td>IBEIS_PZ_1561</td>
      <td>[]</td>
    </tr>
    <tr>
      <th>2</th>
      <td>[981.0, 552.5, 1131.0, 750.0]</td>
      <td>0.0</td>
      <td>left</td>
      <td>[[981, 552, 2112, 552, 2112, 1302, 981, 1302, ...</td>
      <td>[981, 552, 1131, 750]</td>
      <td>848250</td>
      <td>0</td>
      <td>3</td>
      <td>3</td>
      <td>1</td>
      <td>34a7063e-2d17-430d-8f9d-ca7199db248b</td>
      <td>[2, 1, 3, 3459]</td>
      <td>0</td>
      <td>IBEIS_PZ_1561</td>
      <td>[]</td>
    </tr>
    <tr>
      <th>3</th>
      <td>[432.5, 531.0, 1740.0, 938.5]</td>
      <td>0.0</td>
      <td>left</td>
      <td>[[432, 531, 2172, 531, 2172, 1470, 432, 1470, ...</td>
      <td>[432, 531, 1740, 939]</td>
      <td>1633860</td>
      <td>0</td>
      <td>4</td>
      <td>4</td>
      <td>1</td>
      <td>69084074-31c8-4f67-a9b1-9b8d6e414200</td>
      <td>[4]</td>
      <td>0</td>
      <td>IBEIS_PZ_1563</td>
      <td>[]</td>
    </tr>
    <tr>
      <th>4</th>
      <td>[1568.5, 942.5, 450.0, 462.5]</td>
      <td>0.0</td>
      <td>left</td>
      <td>[[1568, 942, 2018, 942, 2018, 1405, 1568, 1405...</td>
      <td>[1568, 942, 450, 463]</td>
      <td>208350</td>
      <td>0</td>
      <td>5</td>
      <td>5</td>
      <td>0</td>
      <td>fa24706c-e90c-4594-9e74-2517997a6c83</td>
      <td>[6, 7, 5, 2126, 2270]</td>
      <td>0</td>
      <td>NNP_GIRM_0140</td>
      <td>[]</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>6920</th>
      <td>[1084.2696629213483, 0.0, 1152.3876404494383, ...</td>
      <td>0.0</td>
      <td>left</td>
      <td>[[1084, 0, 2237, 0, 2237, 1183, 1084, 1183, 10...</td>
      <td>[1084, 0, 1153, 1183]</td>
      <td>1363999</td>
      <td>0</td>
      <td>6921</td>
      <td>4944</td>
      <td>0</td>
      <td>c2fc89c7-0fd0-4aa8-8b15-fee93e004e55</td>
      <td>[4724, 6921, 4971]</td>
      <td>0</td>
      <td>NNP_GIRM_0074</td>
      <td>[]</td>
    </tr>
    <tr>
      <th>6921</th>
      <td>[779.494382022472, 363.76404494382024, 681.179...</td>
      <td>0.0</td>
      <td>left</td>
      <td>[[779, 364, 1461, 364, 1461, 1645, 779, 1645, ...</td>
      <td>[779, 364, 682, 1281]</td>
      <td>873642</td>
      <td>0</td>
      <td>6922</td>
      <td>4945</td>
      <td>0</td>
      <td>30b66e0c-3c35-496a-ad61-de617ef6cbc0</td>
      <td>[6923, 6922]</td>
      <td>0</td>
      <td>NNP_GIRM_0030</td>
      <td>[]</td>
    </tr>
    <tr>
      <th>6922</th>
      <td>[1358.1460674157304, 0.0, 912.2191011235956, 1...</td>
      <td>0.0</td>
      <td>left</td>
      <td>[[1358, 0, 2270, 0, 2270, 1586, 1358, 1586, 13...</td>
      <td>[1358, 0, 912, 1586]</td>
      <td>1446432</td>
      <td>0</td>
      <td>6923</td>
      <td>4946</td>
      <td>0</td>
      <td>5aad1203-9dff-4c2d-a137-539a1050593c</td>
      <td>[6923, 6922]</td>
      <td>0</td>
      <td>NNP_GIRM_0030</td>
      <td>[]</td>
    </tr>
    <tr>
      <th>6923</th>
      <td>[1221.2078651685395, 231.03932584269666, 458.5...</td>
      <td>0.0</td>
      <td>front</td>
      <td>[[1221, 231, 1680, 231, 1680, 1666, 1221, 1666...</td>
      <td>[1221, 231, 459, 1435]</td>
      <td>658665</td>
      <td>0</td>
      <td>6924</td>
      <td>4947</td>
      <td>0</td>
      <td>e6c0d758-9134-478b-a225-e175ff37b217</td>
      <td>[6925, 6924]</td>
      <td>0</td>
      <td>NNP_GIRM_0069</td>
      <td>[]</td>
    </tr>
    <tr>
      <th>6924</th>
      <td>[1127.1067415730338, 37.921348314606746, 689.6...</td>
      <td>0.0</td>
      <td>frontleft</td>
      <td>[[1127, 38, 1817, 38, 1817, 1640, 1127, 1640, ...</td>
      <td>[1127, 38, 690, 1602]</td>
      <td>1105380</td>
      <td>0</td>
      <td>6925</td>
      <td>4948</td>
      <td>0</td>
      <td>48167116-a7bd-4107-be4f-4bd9cd4e1ae7</td>
      <td>[6925, 6924]</td>
      <td>0</td>
      <td>NNP_GIRM_0069</td>
      <td>[]</td>
    </tr>
  </tbody>
</table>
<p>6925 rows × 15 columns</p>
</div>
    <div class="colab-df-buttons">

  <div class="colab-df-container">
    <button class="colab-df-convert" onclick="convertToInteractive('df-92735753-2e56-4e20-aff9-d2785ae468da')"
            title="Convert this dataframe to an interactive table."
            style="display:none;">

  <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960">
    <path d="M120-120v-720h720v720H120Zm60-500h600v-160H180v160Zm220 220h160v-160H400v160Zm0 220h160v-160H400v160ZM180-400h160v-160H180v160Zm440 0h160v-160H620v160ZM180-180h160v-160H180v160Zm440 0h160v-160H620v160Z"/>
  </svg>
    </button>

  <style>
    .colab-df-container {
      display:flex;
      gap: 12px;
    }

    .colab-df-convert {
      background-color: #E8F0FE;
      border: none;
      border-radius: 50%;
      cursor: pointer;
      display: none;
      fill: #1967D2;
      height: 32px;
      padding: 0 0 0 0;
      width: 32px;
    }

    .colab-df-convert:hover {
      background-color: #E2EBFA;
      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);
      fill: #174EA6;
    }

    .colab-df-buttons div {
      margin-bottom: 4px;
    }

    [theme=dark] .colab-df-convert {
      background-color: #3B4455;
      fill: #D2E3FC;
    }

    [theme=dark] .colab-df-convert:hover {
      background-color: #434B5C;
      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);
      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));
      fill: #FFFFFF;
    }
  </style>

    <script>
      const buttonEl =
        document.querySelector('#df-92735753-2e56-4e20-aff9-d2785ae468da button.colab-df-convert');
      buttonEl.style.display =
        google.colab.kernel.accessAllowed ? 'block' : 'none';

      async function convertToInteractive(key) {
        const element = document.querySelector('#df-92735753-2e56-4e20-aff9-d2785ae468da');
        const dataTable =
          await google.colab.kernel.invokeFunction('convertToInteractive',
                                                    [key], {});
        if (!dataTable) return;

        const docLinkHtml = 'Like what you see? Visit the ' +
          '<a target="_blank" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'
          + ' to learn more about interactive tables.';
        element.innerHTML = '';
        dataTable['output_type'] = 'display_data';
        await google.colab.output.renderOutput(dataTable, element);
        const docLink = document.createElement('div');
        docLink.innerHTML = docLinkHtml;
        element.appendChild(docLink);
      }
    </script>
  </div>


    <div id="df-f3053e29-28c6-4847-8d3d-48ebba9c1496">
      <button class="colab-df-quickchart" onclick="quickchart('df-f3053e29-28c6-4847-8d3d-48ebba9c1496')"
                title="Suggest charts"
                style="display:none;">

<svg xmlns="http://www.w3.org/2000/svg" height="24px"viewBox="0 0 24 24"
     width="24px">
    <g>
        <path d="M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zM9 17H7v-7h2v7zm4 0h-2V7h2v10zm4 0h-2v-4h2v4z"/>
    </g>
</svg>
      </button>

<style>
  .colab-df-quickchart {
      --bg-color: #E8F0FE;
      --fill-color: #1967D2;
      --hover-bg-color: #E2EBFA;
      --hover-fill-color: #174EA6;
      --disabled-fill-color: #AAA;
      --disabled-bg-color: #DDD;
  }

  [theme=dark] .colab-df-quickchart {
      --bg-color: #3B4455;
      --fill-color: #D2E3FC;
      --hover-bg-color: #434B5C;
      --hover-fill-color: #FFFFFF;
      --disabled-bg-color: #3B4455;
      --disabled-fill-color: #666;
  }

  .colab-df-quickchart {
    background-color: var(--bg-color);
    border: none;
    border-radius: 50%;
    cursor: pointer;
    display: none;
    fill: var(--fill-color);
    height: 32px;
    padding: 0;
    width: 32px;
  }

  .colab-df-quickchart:hover {
    background-color: var(--hover-bg-color);
    box-shadow: 0 1px 2px rgba(60, 64, 67, 0.3), 0 1px 3px 1px rgba(60, 64, 67, 0.15);
    fill: var(--button-hover-fill-color);
  }

  .colab-df-quickchart-complete:disabled,
  .colab-df-quickchart-complete:disabled:hover {
    background-color: var(--disabled-bg-color);
    fill: var(--disabled-fill-color);
    box-shadow: none;
  }

  .colab-df-spinner {
    border: 2px solid var(--fill-color);
    border-color: transparent;
    border-bottom-color: var(--fill-color);
    animation:
      spin 1s steps(1) infinite;
  }

  @keyframes spin {
    0% {
      border-color: transparent;
      border-bottom-color: var(--fill-color);
      border-left-color: var(--fill-color);
    }
    20% {
      border-color: transparent;
      border-left-color: var(--fill-color);
      border-top-color: var(--fill-color);
    }
    30% {
      border-color: transparent;
      border-left-color: var(--fill-color);
      border-top-color: var(--fill-color);
      border-right-color: var(--fill-color);
    }
    40% {
      border-color: transparent;
      border-right-color: var(--fill-color);
      border-top-color: var(--fill-color);
    }
    60% {
      border-color: transparent;
      border-right-color: var(--fill-color);
    }
    80% {
      border-color: transparent;
      border-right-color: var(--fill-color);
      border-bottom-color: var(--fill-color);
    }
    90% {
      border-color: transparent;
      border-bottom-color: var(--fill-color);
    }
  }
</style>

      <script>
        async function quickchart(key) {
          const quickchartButtonEl =
            document.querySelector('#' + key + ' button');
          quickchartButtonEl.disabled = true;  // To prevent multiple clicks.
          quickchartButtonEl.classList.add('colab-df-spinner');
          try {
            const charts = await google.colab.kernel.invokeFunction(
                'suggestCharts', [key], {});
          } catch (error) {
            console.error('Error during call to suggestCharts:', error);
          }
          quickchartButtonEl.classList.remove('colab-df-spinner');
          quickchartButtonEl.classList.add('colab-df-quickchart-complete');
        }
        (() => {
          let quickchartButtonEl =
            document.querySelector('#df-f3053e29-28c6-4847-8d3d-48ebba9c1496 button');
          quickchartButtonEl.style.display =
            google.colab.kernel.accessAllowed ? 'block' : 'none';
        })();
      </script>
    </div>

  <div id="id_16db8dc6-0eb4-4d9d-af3c-c8ebe61aa507">
    <style>
      .colab-df-generate {
        background-color: #E8F0FE;
        border: none;
        border-radius: 50%;
        cursor: pointer;
        display: none;
        fill: #1967D2;
        height: 32px;
        padding: 0 0 0 0;
        width: 32px;
      }

      .colab-df-generate:hover {
        background-color: #E2EBFA;
        box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);
        fill: #174EA6;
      }

      [theme=dark] .colab-df-generate {
        background-color: #3B4455;
        fill: #D2E3FC;
      }

      [theme=dark] .colab-df-generate:hover {
        background-color: #434B5C;
        box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);
        filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));
        fill: #FFFFFF;
      }
    </style>
    <button class="colab-df-generate" onclick="generateWithVariable('annots_df')"
            title="Generate code using this dataframe."
            style="display:none;">

  <svg xmlns="http://www.w3.org/2000/svg" height="24px"viewBox="0 0 24 24"
       width="24px">
    <path d="M7,19H8.4L18.45,9,17,7.55,7,17.6ZM5,21V16.75L18.45,3.32a2,2,0,0,1,2.83,0l1.4,1.43a1.91,1.91,0,0,1,.58,1.4,1.91,1.91,0,0,1-.58,1.4L9.25,21ZM18.45,9,17,7.55Zm-12,3A5.31,5.31,0,0,0,4.9,8.1,5.31,5.31,0,0,0,1,6.5,5.31,5.31,0,0,0,4.9,4.9,5.31,5.31,0,0,0,6.5,1,5.31,5.31,0,0,0,8.1,4.9,5.31,5.31,0,0,0,12,6.5,5.46,5.46,0,0,0,6.5,12Z"/>
  </svg>
    </button>
    <script>
      (() => {
      const buttonEl =
        document.querySelector('#id_16db8dc6-0eb4-4d9d-af3c-c8ebe61aa507 button.colab-df-generate');
      buttonEl.style.display =
        google.colab.kernel.accessAllowed ? 'block' : 'none';

      buttonEl.onclick = () => {
        google.colab.notebook.generateWithVariable('annots_df');
      }
      })();
    </script>
  </div>

    </div>
  </div>





```python
images_df.columns
```




    Index(['license', 'file_name', 'photographer', 'coco_url', 'height', 'width',
           'date_captured', 'gps_lat_captured', 'gps_lon_captured', 'flickr_url',
           'id', 'uuid'],
          dtype='object')




```python
merged_df = pd.merge(images_df, annots_df, left_on='id', right_on='image_id')
merged_df
```





  <div id="df-87fb9048-01ea-4cd0-8640-c28a65586b24" class="colab-df-container">
    <div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>license</th>
      <th>file_name</th>
      <th>photographer</th>
      <th>coco_url</th>
      <th>height</th>
      <th>width</th>
      <th>date_captured</th>
      <th>gps_lat_captured</th>
      <th>gps_lon_captured</th>
      <th>flickr_url</th>
      <th>...</th>
      <th>area</th>
      <th>iscrowd</th>
      <th>id_y</th>
      <th>image_id</th>
      <th>category_id</th>
      <th>uuid_y</th>
      <th>individual_ids</th>
      <th>isinterest</th>
      <th>name</th>
      <th>review_ids</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>3</td>
      <td>000000000001.jpg</td>
      <td>NNP GZC Car '10WHITE', Person 'A', Image 0005</td>
      <td>None</td>
      <td>2000</td>
      <td>3000</td>
      <td>2015-03-01 14:53:46</td>
      <td>-1.351341</td>
      <td>36.800374</td>
      <td>None</td>
      <td>...</td>
      <td>841800</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>7cfac6bc-379a-4859-a5c8-b21b06d2fe3d</td>
      <td>[2, 1, 3, 3459]</td>
      <td>0</td>
      <td>IBEIS_PZ_1561</td>
      <td>[]</td>
    </tr>
    <tr>
      <th>1</th>
      <td>3</td>
      <td>000000000002.jpg</td>
      <td>NNP GZC Car '10WHITE', Person 'A', Image 0006</td>
      <td>None</td>
      <td>2000</td>
      <td>3000</td>
      <td>2015-03-01 14:53:46</td>
      <td>-1.351341</td>
      <td>36.800374</td>
      <td>None</td>
      <td>...</td>
      <td>859491</td>
      <td>0</td>
      <td>2</td>
      <td>2</td>
      <td>1</td>
      <td>f56434d5-d829-4b56-a511-6e6c91b2f4fd</td>
      <td>[2, 1, 3, 3459]</td>
      <td>0</td>
      <td>IBEIS_PZ_1561</td>
      <td>[]</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>000000000003.jpg</td>
      <td>NNP GZC Car '10WHITE', Person 'A', Image 0007</td>
      <td>None</td>
      <td>2000</td>
      <td>3000</td>
      <td>2015-03-01 14:53:52</td>
      <td>-1.351341</td>
      <td>36.800374</td>
      <td>None</td>
      <td>...</td>
      <td>848250</td>
      <td>0</td>
      <td>3</td>
      <td>3</td>
      <td>1</td>
      <td>34a7063e-2d17-430d-8f9d-ca7199db248b</td>
      <td>[2, 1, 3, 3459]</td>
      <td>0</td>
      <td>IBEIS_PZ_1561</td>
      <td>[]</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>000000000004.jpg</td>
      <td>NNP GZC Car '10WHITE', Person 'A', Image 0008</td>
      <td>None</td>
      <td>2000</td>
      <td>3000</td>
      <td>2015-03-01 14:53:58</td>
      <td>-1.351341</td>
      <td>36.800374</td>
      <td>None</td>
      <td>...</td>
      <td>1633860</td>
      <td>0</td>
      <td>4</td>
      <td>4</td>
      <td>1</td>
      <td>69084074-31c8-4f67-a9b1-9b8d6e414200</td>
      <td>[4]</td>
      <td>0</td>
      <td>IBEIS_PZ_1563</td>
      <td>[]</td>
    </tr>
    <tr>
      <th>4</th>
      <td>3</td>
      <td>000000000005.jpg</td>
      <td>NNP GZC Car '10WHITE', Person 'A', Image 0010</td>
      <td>None</td>
      <td>2000</td>
      <td>3000</td>
      <td>2015-03-01 15:02:32</td>
      <td>-1.367088</td>
      <td>36.781978</td>
      <td>None</td>
      <td>...</td>
      <td>208350</td>
      <td>0</td>
      <td>5</td>
      <td>5</td>
      <td>0</td>
      <td>fa24706c-e90c-4594-9e74-2517997a6c83</td>
      <td>[6, 7, 5, 2126, 2270]</td>
      <td>0</td>
      <td>NNP_GIRM_0140</td>
      <td>[]</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>6920</th>
      <td>3</td>
      <td>000000004944.jpg</td>
      <td></td>
      <td>None</td>
      <td>2000</td>
      <td>3000</td>
      <td>2015-02-26 13:50:34</td>
      <td>-1.376729</td>
      <td>36.830786</td>
      <td>None</td>
      <td>...</td>
      <td>1363999</td>
      <td>0</td>
      <td>6921</td>
      <td>4944</td>
      <td>0</td>
      <td>c2fc89c7-0fd0-4aa8-8b15-fee93e004e55</td>
      <td>[4724, 6921, 4971]</td>
      <td>0</td>
      <td>NNP_GIRM_0074</td>
      <td>[]</td>
    </tr>
    <tr>
      <th>6921</th>
      <td>3</td>
      <td>000000004945.jpg</td>
      <td></td>
      <td>None</td>
      <td>2000</td>
      <td>3000</td>
      <td>2015-02-26 13:50:40</td>
      <td>-1.370916</td>
      <td>36.791815</td>
      <td>None</td>
      <td>...</td>
      <td>873642</td>
      <td>0</td>
      <td>6922</td>
      <td>4945</td>
      <td>0</td>
      <td>30b66e0c-3c35-496a-ad61-de617ef6cbc0</td>
      <td>[6923, 6922]</td>
      <td>0</td>
      <td>NNP_GIRM_0030</td>
      <td>[]</td>
    </tr>
    <tr>
      <th>6922</th>
      <td>3</td>
      <td>000000004946.jpg</td>
      <td></td>
      <td>None</td>
      <td>2000</td>
      <td>3000</td>
      <td>2015-02-26 13:50:50</td>
      <td>-1.370916</td>
      <td>36.791815</td>
      <td>None</td>
      <td>...</td>
      <td>1446432</td>
      <td>0</td>
      <td>6923</td>
      <td>4946</td>
      <td>0</td>
      <td>5aad1203-9dff-4c2d-a137-539a1050593c</td>
      <td>[6923, 6922]</td>
      <td>0</td>
      <td>NNP_GIRM_0030</td>
      <td>[]</td>
    </tr>
    <tr>
      <th>6923</th>
      <td>3</td>
      <td>000000004947.jpg</td>
      <td></td>
      <td>None</td>
      <td>2000</td>
      <td>3000</td>
      <td>2015-02-26 13:51:10</td>
      <td>-1.370916</td>
      <td>36.791815</td>
      <td>None</td>
      <td>...</td>
      <td>658665</td>
      <td>0</td>
      <td>6924</td>
      <td>4947</td>
      <td>0</td>
      <td>e6c0d758-9134-478b-a225-e175ff37b217</td>
      <td>[6925, 6924]</td>
      <td>0</td>
      <td>NNP_GIRM_0069</td>
      <td>[]</td>
    </tr>
    <tr>
      <th>6924</th>
      <td>3</td>
      <td>000000004948.jpg</td>
      <td></td>
      <td>None</td>
      <td>2000</td>
      <td>3000</td>
      <td>2015-02-26 13:51:17</td>
      <td>-1.370916</td>
      <td>36.791815</td>
      <td>None</td>
      <td>...</td>
      <td>1105380</td>
      <td>0</td>
      <td>6925</td>
      <td>4948</td>
      <td>0</td>
      <td>48167116-a7bd-4107-be4f-4bd9cd4e1ae7</td>
      <td>[6925, 6924]</td>
      <td>0</td>
      <td>NNP_GIRM_0069</td>
      <td>[]</td>
    </tr>
  </tbody>
</table>
<p>6925 rows × 27 columns</p>
</div>
    <div class="colab-df-buttons">

  <div class="colab-df-container">
    <button class="colab-df-convert" onclick="convertToInteractive('df-87fb9048-01ea-4cd0-8640-c28a65586b24')"
            title="Convert this dataframe to an interactive table."
            style="display:none;">

  <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960">
    <path d="M120-120v-720h720v720H120Zm60-500h600v-160H180v160Zm220 220h160v-160H400v160Zm0 220h160v-160H400v160ZM180-400h160v-160H180v160Zm440 0h160v-160H620v160ZM180-180h160v-160H180v160Zm440 0h160v-160H620v160Z"/>
  </svg>
    </button>

  <style>
    .colab-df-container {
      display:flex;
      gap: 12px;
    }

    .colab-df-convert {
      background-color: #E8F0FE;
      border: none;
      border-radius: 50%;
      cursor: pointer;
      display: none;
      fill: #1967D2;
      height: 32px;
      padding: 0 0 0 0;
      width: 32px;
    }

    .colab-df-convert:hover {
      background-color: #E2EBFA;
      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);
      fill: #174EA6;
    }

    .colab-df-buttons div {
      margin-bottom: 4px;
    }

    [theme=dark] .colab-df-convert {
      background-color: #3B4455;
      fill: #D2E3FC;
    }

    [theme=dark] .colab-df-convert:hover {
      background-color: #434B5C;
      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);
      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));
      fill: #FFFFFF;
    }
  </style>

    <script>
      const buttonEl =
        document.querySelector('#df-87fb9048-01ea-4cd0-8640-c28a65586b24 button.colab-df-convert');
      buttonEl.style.display =
        google.colab.kernel.accessAllowed ? 'block' : 'none';

      async function convertToInteractive(key) {
        const element = document.querySelector('#df-87fb9048-01ea-4cd0-8640-c28a65586b24');
        const dataTable =
          await google.colab.kernel.invokeFunction('convertToInteractive',
                                                    [key], {});
        if (!dataTable) return;

        const docLinkHtml = 'Like what you see? Visit the ' +
          '<a target="_blank" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'
          + ' to learn more about interactive tables.';
        element.innerHTML = '';
        dataTable['output_type'] = 'display_data';
        await google.colab.output.renderOutput(dataTable, element);
        const docLink = document.createElement('div');
        docLink.innerHTML = docLinkHtml;
        element.appendChild(docLink);
      }
    </script>
  </div>


    <div id="df-3bd64df0-c897-47f7-b32f-877a34c228f6">
      <button class="colab-df-quickchart" onclick="quickchart('df-3bd64df0-c897-47f7-b32f-877a34c228f6')"
                title="Suggest charts"
                style="display:none;">

<svg xmlns="http://www.w3.org/2000/svg" height="24px"viewBox="0 0 24 24"
     width="24px">
    <g>
        <path d="M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zM9 17H7v-7h2v7zm4 0h-2V7h2v10zm4 0h-2v-4h2v4z"/>
    </g>
</svg>
      </button>

<style>
  .colab-df-quickchart {
      --bg-color: #E8F0FE;
      --fill-color: #1967D2;
      --hover-bg-color: #E2EBFA;
      --hover-fill-color: #174EA6;
      --disabled-fill-color: #AAA;
      --disabled-bg-color: #DDD;
  }

  [theme=dark] .colab-df-quickchart {
      --bg-color: #3B4455;
      --fill-color: #D2E3FC;
      --hover-bg-color: #434B5C;
      --hover-fill-color: #FFFFFF;
      --disabled-bg-color: #3B4455;
      --disabled-fill-color: #666;
  }

  .colab-df-quickchart {
    background-color: var(--bg-color);
    border: none;
    border-radius: 50%;
    cursor: pointer;
    display: none;
    fill: var(--fill-color);
    height: 32px;
    padding: 0;
    width: 32px;
  }

  .colab-df-quickchart:hover {
    background-color: var(--hover-bg-color);
    box-shadow: 0 1px 2px rgba(60, 64, 67, 0.3), 0 1px 3px 1px rgba(60, 64, 67, 0.15);
    fill: var(--button-hover-fill-color);
  }

  .colab-df-quickchart-complete:disabled,
  .colab-df-quickchart-complete:disabled:hover {
    background-color: var(--disabled-bg-color);
    fill: var(--disabled-fill-color);
    box-shadow: none;
  }

  .colab-df-spinner {
    border: 2px solid var(--fill-color);
    border-color: transparent;
    border-bottom-color: var(--fill-color);
    animation:
      spin 1s steps(1) infinite;
  }

  @keyframes spin {
    0% {
      border-color: transparent;
      border-bottom-color: var(--fill-color);
      border-left-color: var(--fill-color);
    }
    20% {
      border-color: transparent;
      border-left-color: var(--fill-color);
      border-top-color: var(--fill-color);
    }
    30% {
      border-color: transparent;
      border-left-color: var(--fill-color);
      border-top-color: var(--fill-color);
      border-right-color: var(--fill-color);
    }
    40% {
      border-color: transparent;
      border-right-color: var(--fill-color);
      border-top-color: var(--fill-color);
    }
    60% {
      border-color: transparent;
      border-right-color: var(--fill-color);
    }
    80% {
      border-color: transparent;
      border-right-color: var(--fill-color);
      border-bottom-color: var(--fill-color);
    }
    90% {
      border-color: transparent;
      border-bottom-color: var(--fill-color);
    }
  }
</style>

      <script>
        async function quickchart(key) {
          const quickchartButtonEl =
            document.querySelector('#' + key + ' button');
          quickchartButtonEl.disabled = true;  // To prevent multiple clicks.
          quickchartButtonEl.classList.add('colab-df-spinner');
          try {
            const charts = await google.colab.kernel.invokeFunction(
                'suggestCharts', [key], {});
          } catch (error) {
            console.error('Error during call to suggestCharts:', error);
          }
          quickchartButtonEl.classList.remove('colab-df-spinner');
          quickchartButtonEl.classList.add('colab-df-quickchart-complete');
        }
        (() => {
          let quickchartButtonEl =
            document.querySelector('#df-3bd64df0-c897-47f7-b32f-877a34c228f6 button');
          quickchartButtonEl.style.display =
            google.colab.kernel.accessAllowed ? 'block' : 'none';
        })();
      </script>
    </div>

  <div id="id_c224865e-4246-4a8a-a7ed-e93e61f42d17">
    <style>
      .colab-df-generate {
        background-color: #E8F0FE;
        border: none;
        border-radius: 50%;
        cursor: pointer;
        display: none;
        fill: #1967D2;
        height: 32px;
        padding: 0 0 0 0;
        width: 32px;
      }

      .colab-df-generate:hover {
        background-color: #E2EBFA;
        box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);
        fill: #174EA6;
      }

      [theme=dark] .colab-df-generate {
        background-color: #3B4455;
        fill: #D2E3FC;
      }

      [theme=dark] .colab-df-generate:hover {
        background-color: #434B5C;
        box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);
        filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));
        fill: #FFFFFF;
      }
    </style>
    <button class="colab-df-generate" onclick="generateWithVariable('merged_df')"
            title="Generate code using this dataframe."
            style="display:none;">

  <svg xmlns="http://www.w3.org/2000/svg" height="24px"viewBox="0 0 24 24"
       width="24px">
    <path d="M7,19H8.4L18.45,9,17,7.55,7,17.6ZM5,21V16.75L18.45,3.32a2,2,0,0,1,2.83,0l1.4,1.43a1.91,1.91,0,0,1,.58,1.4,1.91,1.91,0,0,1-.58,1.4L9.25,21ZM18.45,9,17,7.55Zm-12,3A5.31,5.31,0,0,0,4.9,8.1,5.31,5.31,0,0,0,1,6.5,5.31,5.31,0,0,0,4.9,4.9,5.31,5.31,0,0,0,6.5,1,5.31,5.31,0,0,0,8.1,4.9,5.31,5.31,0,0,0,12,6.5,5.46,5.46,0,0,0,6.5,12Z"/>
  </svg>
    </button>
    <script>
      (() => {
      const buttonEl =
        document.querySelector('#id_c224865e-4246-4a8a-a7ed-e93e61f42d17 button.colab-df-generate');
      buttonEl.style.display =
        google.colab.kernel.accessAllowed ? 'block' : 'none';

      buttonEl.onclick = () => {
        google.colab.notebook.generateWithVariable('merged_df');
      }
      })();
    </script>
  </div>

    </div>
  </div>





```python
merged_df.columns
```




    Index(['license', 'file_name', 'photographer', 'coco_url', 'height', 'width',
           'date_captured', 'gps_lat_captured', 'gps_lon_captured', 'flickr_url',
           'id_x', 'uuid_x', 'bbox', 'theta', 'viewpoint', 'segmentation',
           'segmentation_bbox', 'area', 'iscrowd', 'id_y', 'image_id',
           'category_id', 'uuid_y', 'individual_ids', 'isinterest', 'name',
           'review_ids'],
          dtype='object')




```python
row = merged_df.loc[merged_df['file_name']==img_path.name]
row
```





  <div id="df-2c143193-5659-49af-9ae9-0013ca435622" class="colab-df-container">
    <div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>license</th>
      <th>file_name</th>
      <th>photographer</th>
      <th>coco_url</th>
      <th>height</th>
      <th>width</th>
      <th>date_captured</th>
      <th>gps_lat_captured</th>
      <th>gps_lon_captured</th>
      <th>flickr_url</th>
      <th>...</th>
      <th>area</th>
      <th>iscrowd</th>
      <th>id_y</th>
      <th>image_id</th>
      <th>category_id</th>
      <th>uuid_y</th>
      <th>individual_ids</th>
      <th>isinterest</th>
      <th>name</th>
      <th>review_ids</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>6912</th>
      <td>3</td>
      <td>000000004938.jpg</td>
      <td></td>
      <td>None</td>
      <td>2000</td>
      <td>3000</td>
      <td>2015-02-26 13:38:10</td>
      <td>-1.376729</td>
      <td>36.830786</td>
      <td>None</td>
      <td>...</td>
      <td>3594736</td>
      <td>0</td>
      <td>6913</td>
      <td>4938</td>
      <td>0</td>
      <td>da113867-39ee-48cc-8988-334793e24f2c</td>
      <td>[5612, 6913, 5603, 5607, 5615, 5604, 4677, 4675]</td>
      <td>0</td>
      <td>NNP_GIRM_0047</td>
      <td>[]</td>
    </tr>
  </tbody>
</table>
<p>1 rows × 27 columns</p>
</div>
    <div class="colab-df-buttons">

  <div class="colab-df-container">
    <button class="colab-df-convert" onclick="convertToInteractive('df-2c143193-5659-49af-9ae9-0013ca435622')"
            title="Convert this dataframe to an interactive table."
            style="display:none;">

  <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960">
    <path d="M120-120v-720h720v720H120Zm60-500h600v-160H180v160Zm220 220h160v-160H400v160Zm0 220h160v-160H400v160ZM180-400h160v-160H180v160Zm440 0h160v-160H620v160ZM180-180h160v-160H180v160Zm440 0h160v-160H620v160Z"/>
  </svg>
    </button>

  <style>
    .colab-df-container {
      display:flex;
      gap: 12px;
    }

    .colab-df-convert {
      background-color: #E8F0FE;
      border: none;
      border-radius: 50%;
      cursor: pointer;
      display: none;
      fill: #1967D2;
      height: 32px;
      padding: 0 0 0 0;
      width: 32px;
    }

    .colab-df-convert:hover {
      background-color: #E2EBFA;
      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);
      fill: #174EA6;
    }

    .colab-df-buttons div {
      margin-bottom: 4px;
    }

    [theme=dark] .colab-df-convert {
      background-color: #3B4455;
      fill: #D2E3FC;
    }

    [theme=dark] .colab-df-convert:hover {
      background-color: #434B5C;
      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);
      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));
      fill: #FFFFFF;
    }
  </style>

    <script>
      const buttonEl =
        document.querySelector('#df-2c143193-5659-49af-9ae9-0013ca435622 button.colab-df-convert');
      buttonEl.style.display =
        google.colab.kernel.accessAllowed ? 'block' : 'none';

      async function convertToInteractive(key) {
        const element = document.querySelector('#df-2c143193-5659-49af-9ae9-0013ca435622');
        const dataTable =
          await google.colab.kernel.invokeFunction('convertToInteractive',
                                                    [key], {});
        if (!dataTable) return;

        const docLinkHtml = 'Like what you see? Visit the ' +
          '<a target="_blank" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'
          + ' to learn more about interactive tables.';
        element.innerHTML = '';
        dataTable['output_type'] = 'display_data';
        await google.colab.output.renderOutput(dataTable, element);
        const docLink = document.createElement('div');
        docLink.innerHTML = docLinkHtml;
        element.appendChild(docLink);
      }
    </script>
  </div>


  <div id="id_5a1107d3-9539-45f7-9113-51c7a5b31541">
    <style>
      .colab-df-generate {
        background-color: #E8F0FE;
        border: none;
        border-radius: 50%;
        cursor: pointer;
        display: none;
        fill: #1967D2;
        height: 32px;
        padding: 0 0 0 0;
        width: 32px;
      }

      .colab-df-generate:hover {
        background-color: #E2EBFA;
        box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);
        fill: #174EA6;
      }

      [theme=dark] .colab-df-generate {
        background-color: #3B4455;
        fill: #D2E3FC;
      }

      [theme=dark] .colab-df-generate:hover {
        background-color: #434B5C;
        box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);
        filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));
        fill: #FFFFFF;
      }
    </style>
    <button class="colab-df-generate" onclick="generateWithVariable('row')"
            title="Generate code using this dataframe."
            style="display:none;">

  <svg xmlns="http://www.w3.org/2000/svg" height="24px"viewBox="0 0 24 24"
       width="24px">
    <path d="M7,19H8.4L18.45,9,17,7.55,7,17.6ZM5,21V16.75L18.45,3.32a2,2,0,0,1,2.83,0l1.4,1.43a1.91,1.91,0,0,1,.58,1.4,1.91,1.91,0,0,1-.58,1.4L9.25,21ZM18.45,9,17,7.55Zm-12,3A5.31,5.31,0,0,0,4.9,8.1,5.31,5.31,0,0,0,1,6.5,5.31,5.31,0,0,0,4.9,4.9,5.31,5.31,0,0,0,6.5,1,5.31,5.31,0,0,0,8.1,4.9,5.31,5.31,0,0,0,12,6.5,5.46,5.46,0,0,0,6.5,12Z"/>
  </svg>
    </button>
    <script>
      (() => {
      const buttonEl =
        document.querySelector('#id_5a1107d3-9539-45f7-9113-51c7a5b31541 button.colab-df-generate');
      buttonEl.style.display =
        google.colab.kernel.accessAllowed ? 'block' : 'none';

      buttonEl.onclick = () => {
        google.colab.notebook.generateWithVariable('row');
      }
      })();
    </script>
  </div>

    </div>
  </div>





```python
# merged_df[merged_df['file_name']==img_path.name]
```


```python
from pathlib import Path
image_paths = Path('gzgc.coco/images').rglob('**/*.jpg')
image_paths = list(image_paths)
print(f'Found {len(image_paths)} images')

data_dict_list = []
for img_path in image_paths[:10]:
    split, filename = img_path.parts[-2:]
    row = merged_df.loc[merged_df['file_name']==filename]
    data_dict = {
        'split': split,
        # 'identity': identity,
        'filename': filename,
        'filepath': img_path.as_posix()
    }
    data_dict_list.append(data_dict)
```

    Found 4948 images



```python
import pandas as pd

df = pd.DataFrame(data_dict_list)
df
```





  <div id="df-1a04f46a-04e4-4e29-a533-55834b4ae9b6" class="colab-df-container">
    <div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>split</th>
      <th>filename</th>
      <th>filepath</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>train2020</td>
      <td>000000002284.jpg</td>
      <td>gzgc.coco/images/train2020/000000002284.jpg</td>
    </tr>
    <tr>
      <th>1</th>
      <td>train2020</td>
      <td>000000004822.jpg</td>
      <td>gzgc.coco/images/train2020/000000004822.jpg</td>
    </tr>
    <tr>
      <th>2</th>
      <td>train2020</td>
      <td>000000000540.jpg</td>
      <td>gzgc.coco/images/train2020/000000000540.jpg</td>
    </tr>
    <tr>
      <th>3</th>
      <td>train2020</td>
      <td>000000004938.jpg</td>
      <td>gzgc.coco/images/train2020/000000004938.jpg</td>
    </tr>
    <tr>
      <th>4</th>
      <td>train2020</td>
      <td>000000004400.jpg</td>
      <td>gzgc.coco/images/train2020/000000004400.jpg</td>
    </tr>
    <tr>
      <th>5</th>
      <td>train2020</td>
      <td>000000003650.jpg</td>
      <td>gzgc.coco/images/train2020/000000003650.jpg</td>
    </tr>
    <tr>
      <th>6</th>
      <td>train2020</td>
      <td>000000000597.jpg</td>
      <td>gzgc.coco/images/train2020/000000000597.jpg</td>
    </tr>
    <tr>
      <th>7</th>
      <td>train2020</td>
      <td>000000003693.jpg</td>
      <td>gzgc.coco/images/train2020/000000003693.jpg</td>
    </tr>
    <tr>
      <th>8</th>
      <td>train2020</td>
      <td>000000004670.jpg</td>
      <td>gzgc.coco/images/train2020/000000004670.jpg</td>
    </tr>
    <tr>
      <th>9</th>
      <td>train2020</td>
      <td>000000000069.jpg</td>
      <td>gzgc.coco/images/train2020/000000000069.jpg</td>
    </tr>
  </tbody>
</table>
</div>
    <div class="colab-df-buttons">

  <div class="colab-df-container">
    <button class="colab-df-convert" onclick="convertToInteractive('df-1a04f46a-04e4-4e29-a533-55834b4ae9b6')"
            title="Convert this dataframe to an interactive table."
            style="display:none;">

  <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960">
    <path d="M120-120v-720h720v720H120Zm60-500h600v-160H180v160Zm220 220h160v-160H400v160Zm0 220h160v-160H400v160ZM180-400h160v-160H180v160Zm440 0h160v-160H620v160ZM180-180h160v-160H180v160Zm440 0h160v-160H620v160Z"/>
  </svg>
    </button>

  <style>
    .colab-df-container {
      display:flex;
      gap: 12px;
    }

    .colab-df-convert {
      background-color: #E8F0FE;
      border: none;
      border-radius: 50%;
      cursor: pointer;
      display: none;
      fill: #1967D2;
      height: 32px;
      padding: 0 0 0 0;
      width: 32px;
    }

    .colab-df-convert:hover {
      background-color: #E2EBFA;
      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);
      fill: #174EA6;
    }

    .colab-df-buttons div {
      margin-bottom: 4px;
    }

    [theme=dark] .colab-df-convert {
      background-color: #3B4455;
      fill: #D2E3FC;
    }

    [theme=dark] .colab-df-convert:hover {
      background-color: #434B5C;
      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);
      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));
      fill: #FFFFFF;
    }
  </style>

    <script>
      const buttonEl =
        document.querySelector('#df-1a04f46a-04e4-4e29-a533-55834b4ae9b6 button.colab-df-convert');
      buttonEl.style.display =
        google.colab.kernel.accessAllowed ? 'block' : 'none';

      async function convertToInteractive(key) {
        const element = document.querySelector('#df-1a04f46a-04e4-4e29-a533-55834b4ae9b6');
        const dataTable =
          await google.colab.kernel.invokeFunction('convertToInteractive',
                                                    [key], {});
        if (!dataTable) return;

        const docLinkHtml = 'Like what you see? Visit the ' +
          '<a target="_blank" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'
          + ' to learn more about interactive tables.';
        element.innerHTML = '';
        dataTable['output_type'] = 'display_data';
        await google.colab.output.renderOutput(dataTable, element);
        const docLink = document.createElement('div');
        docLink.innerHTML = docLinkHtml;
        element.appendChild(docLink);
      }
    </script>
  </div>


    <div id="df-58965148-b9b5-4d1e-9e98-1a855a3780bb">
      <button class="colab-df-quickchart" onclick="quickchart('df-58965148-b9b5-4d1e-9e98-1a855a3780bb')"
                title="Suggest charts"
                style="display:none;">

<svg xmlns="http://www.w3.org/2000/svg" height="24px"viewBox="0 0 24 24"
     width="24px">
    <g>
        <path d="M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zM9 17H7v-7h2v7zm4 0h-2V7h2v10zm4 0h-2v-4h2v4z"/>
    </g>
</svg>
      </button>

<style>
  .colab-df-quickchart {
      --bg-color: #E8F0FE;
      --fill-color: #1967D2;
      --hover-bg-color: #E2EBFA;
      --hover-fill-color: #174EA6;
      --disabled-fill-color: #AAA;
      --disabled-bg-color: #DDD;
  }

  [theme=dark] .colab-df-quickchart {
      --bg-color: #3B4455;
      --fill-color: #D2E3FC;
      --hover-bg-color: #434B5C;
      --hover-fill-color: #FFFFFF;
      --disabled-bg-color: #3B4455;
      --disabled-fill-color: #666;
  }

  .colab-df-quickchart {
    background-color: var(--bg-color);
    border: none;
    border-radius: 50%;
    cursor: pointer;
    display: none;
    fill: var(--fill-color);
    height: 32px;
    padding: 0;
    width: 32px;
  }

  .colab-df-quickchart:hover {
    background-color: var(--hover-bg-color);
    box-shadow: 0 1px 2px rgba(60, 64, 67, 0.3), 0 1px 3px 1px rgba(60, 64, 67, 0.15);
    fill: var(--button-hover-fill-color);
  }

  .colab-df-quickchart-complete:disabled,
  .colab-df-quickchart-complete:disabled:hover {
    background-color: var(--disabled-bg-color);
    fill: var(--disabled-fill-color);
    box-shadow: none;
  }

  .colab-df-spinner {
    border: 2px solid var(--fill-color);
    border-color: transparent;
    border-bottom-color: var(--fill-color);
    animation:
      spin 1s steps(1) infinite;
  }

  @keyframes spin {
    0% {
      border-color: transparent;
      border-bottom-color: var(--fill-color);
      border-left-color: var(--fill-color);
    }
    20% {
      border-color: transparent;
      border-left-color: var(--fill-color);
      border-top-color: var(--fill-color);
    }
    30% {
      border-color: transparent;
      border-left-color: var(--fill-color);
      border-top-color: var(--fill-color);
      border-right-color: var(--fill-color);
    }
    40% {
      border-color: transparent;
      border-right-color: var(--fill-color);
      border-top-color: var(--fill-color);
    }
    60% {
      border-color: transparent;
      border-right-color: var(--fill-color);
    }
    80% {
      border-color: transparent;
      border-right-color: var(--fill-color);
      border-bottom-color: var(--fill-color);
    }
    90% {
      border-color: transparent;
      border-bottom-color: var(--fill-color);
    }
  }
</style>

      <script>
        async function quickchart(key) {
          const quickchartButtonEl =
            document.querySelector('#' + key + ' button');
          quickchartButtonEl.disabled = true;  // To prevent multiple clicks.
          quickchartButtonEl.classList.add('colab-df-spinner');
          try {
            const charts = await google.colab.kernel.invokeFunction(
                'suggestCharts', [key], {});
          } catch (error) {
            console.error('Error during call to suggestCharts:', error);
          }
          quickchartButtonEl.classList.remove('colab-df-spinner');
          quickchartButtonEl.classList.add('colab-df-quickchart-complete');
        }
        (() => {
          let quickchartButtonEl =
            document.querySelector('#df-58965148-b9b5-4d1e-9e98-1a855a3780bb button');
          quickchartButtonEl.style.display =
            google.colab.kernel.accessAllowed ? 'block' : 'none';
        })();
      </script>
    </div>

  <div id="id_3e52c9f0-47b2-4bd3-9627-119f8b7216e8">
    <style>
      .colab-df-generate {
        background-color: #E8F0FE;
        border: none;
        border-radius: 50%;
        cursor: pointer;
        display: none;
        fill: #1967D2;
        height: 32px;
        padding: 0 0 0 0;
        width: 32px;
      }

      .colab-df-generate:hover {
        background-color: #E2EBFA;
        box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);
        fill: #174EA6;
      }

      [theme=dark] .colab-df-generate {
        background-color: #3B4455;
        fill: #D2E3FC;
      }

      [theme=dark] .colab-df-generate:hover {
        background-color: #434B5C;
        box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);
        filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));
        fill: #FFFFFF;
      }
    </style>
    <button class="colab-df-generate" onclick="generateWithVariable('df')"
            title="Generate code using this dataframe."
            style="display:none;">

  <svg xmlns="http://www.w3.org/2000/svg" height="24px"viewBox="0 0 24 24"
       width="24px">
    <path d="M7,19H8.4L18.45,9,17,7.55,7,17.6ZM5,21V16.75L18.45,3.32a2,2,0,0,1,2.83,0l1.4,1.43a1.91,1.91,0,0,1,.58,1.4,1.91,1.91,0,0,1-.58,1.4L9.25,21ZM18.45,9,17,7.55Zm-12,3A5.31,5.31,0,0,0,4.9,8.1,5.31,5.31,0,0,0,1,6.5,5.31,5.31,0,0,0,4.9,4.9,5.31,5.31,0,0,0,6.5,1,5.31,5.31,0,0,0,8.1,4.9,5.31,5.31,0,0,0,12,6.5,5.46,5.46,0,0,0,6.5,12Z"/>
  </svg>
    </button>
    <script>
      (() => {
      const buttonEl =
        document.querySelector('#id_3e52c9f0-47b2-4bd3-9627-119f8b7216e8 button.colab-df-generate');
      buttonEl.style.display =
        google.colab.kernel.accessAllowed ? 'block' : 'none';

      buttonEl.onclick = () => {
        google.colab.notebook.generateWithVariable('df');
      }
      })();
    </script>
  </div>

    </div>
  </div>





```python
merged_df.head()
```





  <div id="df-7941cf39-08e3-4e01-8fe4-779c5110e4d3" class="colab-df-container">
    <div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>license</th>
      <th>file_name</th>
      <th>photographer</th>
      <th>coco_url</th>
      <th>height</th>
      <th>width</th>
      <th>date_captured</th>
      <th>gps_lat_captured</th>
      <th>gps_lon_captured</th>
      <th>flickr_url</th>
      <th>...</th>
      <th>area</th>
      <th>iscrowd</th>
      <th>id_y</th>
      <th>image_id</th>
      <th>category_id</th>
      <th>uuid_y</th>
      <th>individual_ids</th>
      <th>isinterest</th>
      <th>name</th>
      <th>review_ids</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>3</td>
      <td>000000000001.jpg</td>
      <td>NNP GZC Car '10WHITE', Person 'A', Image 0005</td>
      <td>None</td>
      <td>2000</td>
      <td>3000</td>
      <td>2015-03-01 14:53:46</td>
      <td>-1.351341</td>
      <td>36.800374</td>
      <td>None</td>
      <td>...</td>
      <td>841800</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>7cfac6bc-379a-4859-a5c8-b21b06d2fe3d</td>
      <td>[2, 1, 3, 3459]</td>
      <td>0</td>
      <td>IBEIS_PZ_1561</td>
      <td>[]</td>
    </tr>
    <tr>
      <th>1</th>
      <td>3</td>
      <td>000000000002.jpg</td>
      <td>NNP GZC Car '10WHITE', Person 'A', Image 0006</td>
      <td>None</td>
      <td>2000</td>
      <td>3000</td>
      <td>2015-03-01 14:53:46</td>
      <td>-1.351341</td>
      <td>36.800374</td>
      <td>None</td>
      <td>...</td>
      <td>859491</td>
      <td>0</td>
      <td>2</td>
      <td>2</td>
      <td>1</td>
      <td>f56434d5-d829-4b56-a511-6e6c91b2f4fd</td>
      <td>[2, 1, 3, 3459]</td>
      <td>0</td>
      <td>IBEIS_PZ_1561</td>
      <td>[]</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>000000000003.jpg</td>
      <td>NNP GZC Car '10WHITE', Person 'A', Image 0007</td>
      <td>None</td>
      <td>2000</td>
      <td>3000</td>
      <td>2015-03-01 14:53:52</td>
      <td>-1.351341</td>
      <td>36.800374</td>
      <td>None</td>
      <td>...</td>
      <td>848250</td>
      <td>0</td>
      <td>3</td>
      <td>3</td>
      <td>1</td>
      <td>34a7063e-2d17-430d-8f9d-ca7199db248b</td>
      <td>[2, 1, 3, 3459]</td>
      <td>0</td>
      <td>IBEIS_PZ_1561</td>
      <td>[]</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>000000000004.jpg</td>
      <td>NNP GZC Car '10WHITE', Person 'A', Image 0008</td>
      <td>None</td>
      <td>2000</td>
      <td>3000</td>
      <td>2015-03-01 14:53:58</td>
      <td>-1.351341</td>
      <td>36.800374</td>
      <td>None</td>
      <td>...</td>
      <td>1633860</td>
      <td>0</td>
      <td>4</td>
      <td>4</td>
      <td>1</td>
      <td>69084074-31c8-4f67-a9b1-9b8d6e414200</td>
      <td>[4]</td>
      <td>0</td>
      <td>IBEIS_PZ_1563</td>
      <td>[]</td>
    </tr>
    <tr>
      <th>4</th>
      <td>3</td>
      <td>000000000005.jpg</td>
      <td>NNP GZC Car '10WHITE', Person 'A', Image 0010</td>
      <td>None</td>
      <td>2000</td>
      <td>3000</td>
      <td>2015-03-01 15:02:32</td>
      <td>-1.367088</td>
      <td>36.781978</td>
      <td>None</td>
      <td>...</td>
      <td>208350</td>
      <td>0</td>
      <td>5</td>
      <td>5</td>
      <td>0</td>
      <td>fa24706c-e90c-4594-9e74-2517997a6c83</td>
      <td>[6, 7, 5, 2126, 2270]</td>
      <td>0</td>
      <td>NNP_GIRM_0140</td>
      <td>[]</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 27 columns</p>
</div>
    <div class="colab-df-buttons">

  <div class="colab-df-container">
    <button class="colab-df-convert" onclick="convertToInteractive('df-7941cf39-08e3-4e01-8fe4-779c5110e4d3')"
            title="Convert this dataframe to an interactive table."
            style="display:none;">

  <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960">
    <path d="M120-120v-720h720v720H120Zm60-500h600v-160H180v160Zm220 220h160v-160H400v160Zm0 220h160v-160H400v160ZM180-400h160v-160H180v160Zm440 0h160v-160H620v160ZM180-180h160v-160H180v160Zm440 0h160v-160H620v160Z"/>
  </svg>
    </button>

  <style>
    .colab-df-container {
      display:flex;
      gap: 12px;
    }

    .colab-df-convert {
      background-color: #E8F0FE;
      border: none;
      border-radius: 50%;
      cursor: pointer;
      display: none;
      fill: #1967D2;
      height: 32px;
      padding: 0 0 0 0;
      width: 32px;
    }

    .colab-df-convert:hover {
      background-color: #E2EBFA;
      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);
      fill: #174EA6;
    }

    .colab-df-buttons div {
      margin-bottom: 4px;
    }

    [theme=dark] .colab-df-convert {
      background-color: #3B4455;
      fill: #D2E3FC;
    }

    [theme=dark] .colab-df-convert:hover {
      background-color: #434B5C;
      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);
      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));
      fill: #FFFFFF;
    }
  </style>

    <script>
      const buttonEl =
        document.querySelector('#df-7941cf39-08e3-4e01-8fe4-779c5110e4d3 button.colab-df-convert');
      buttonEl.style.display =
        google.colab.kernel.accessAllowed ? 'block' : 'none';

      async function convertToInteractive(key) {
        const element = document.querySelector('#df-7941cf39-08e3-4e01-8fe4-779c5110e4d3');
        const dataTable =
          await google.colab.kernel.invokeFunction('convertToInteractive',
                                                    [key], {});
        if (!dataTable) return;

        const docLinkHtml = 'Like what you see? Visit the ' +
          '<a target="_blank" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'
          + ' to learn more about interactive tables.';
        element.innerHTML = '';
        dataTable['output_type'] = 'display_data';
        await google.colab.output.renderOutput(dataTable, element);
        const docLink = document.createElement('div');
        docLink.innerHTML = docLinkHtml;
        element.appendChild(docLink);
      }
    </script>
  </div>


    <div id="df-e4a4bfca-3d70-4bfa-81b3-5795a3ac32e3">
      <button class="colab-df-quickchart" onclick="quickchart('df-e4a4bfca-3d70-4bfa-81b3-5795a3ac32e3')"
                title="Suggest charts"
                style="display:none;">

<svg xmlns="http://www.w3.org/2000/svg" height="24px"viewBox="0 0 24 24"
     width="24px">
    <g>
        <path d="M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zM9 17H7v-7h2v7zm4 0h-2V7h2v10zm4 0h-2v-4h2v4z"/>
    </g>
</svg>
      </button>

<style>
  .colab-df-quickchart {
      --bg-color: #E8F0FE;
      --fill-color: #1967D2;
      --hover-bg-color: #E2EBFA;
      --hover-fill-color: #174EA6;
      --disabled-fill-color: #AAA;
      --disabled-bg-color: #DDD;
  }

  [theme=dark] .colab-df-quickchart {
      --bg-color: #3B4455;
      --fill-color: #D2E3FC;
      --hover-bg-color: #434B5C;
      --hover-fill-color: #FFFFFF;
      --disabled-bg-color: #3B4455;
      --disabled-fill-color: #666;
  }

  .colab-df-quickchart {
    background-color: var(--bg-color);
    border: none;
    border-radius: 50%;
    cursor: pointer;
    display: none;
    fill: var(--fill-color);
    height: 32px;
    padding: 0;
    width: 32px;
  }

  .colab-df-quickchart:hover {
    background-color: var(--hover-bg-color);
    box-shadow: 0 1px 2px rgba(60, 64, 67, 0.3), 0 1px 3px 1px rgba(60, 64, 67, 0.15);
    fill: var(--button-hover-fill-color);
  }

  .colab-df-quickchart-complete:disabled,
  .colab-df-quickchart-complete:disabled:hover {
    background-color: var(--disabled-bg-color);
    fill: var(--disabled-fill-color);
    box-shadow: none;
  }

  .colab-df-spinner {
    border: 2px solid var(--fill-color);
    border-color: transparent;
    border-bottom-color: var(--fill-color);
    animation:
      spin 1s steps(1) infinite;
  }

  @keyframes spin {
    0% {
      border-color: transparent;
      border-bottom-color: var(--fill-color);
      border-left-color: var(--fill-color);
    }
    20% {
      border-color: transparent;
      border-left-color: var(--fill-color);
      border-top-color: var(--fill-color);
    }
    30% {
      border-color: transparent;
      border-left-color: var(--fill-color);
      border-top-color: var(--fill-color);
      border-right-color: var(--fill-color);
    }
    40% {
      border-color: transparent;
      border-right-color: var(--fill-color);
      border-top-color: var(--fill-color);
    }
    60% {
      border-color: transparent;
      border-right-color: var(--fill-color);
    }
    80% {
      border-color: transparent;
      border-right-color: var(--fill-color);
      border-bottom-color: var(--fill-color);
    }
    90% {
      border-color: transparent;
      border-bottom-color: var(--fill-color);
    }
  }
</style>

      <script>
        async function quickchart(key) {
          const quickchartButtonEl =
            document.querySelector('#' + key + ' button');
          quickchartButtonEl.disabled = true;  // To prevent multiple clicks.
          quickchartButtonEl.classList.add('colab-df-spinner');
          try {
            const charts = await google.colab.kernel.invokeFunction(
                'suggestCharts', [key], {});
          } catch (error) {
            console.error('Error during call to suggestCharts:', error);
          }
          quickchartButtonEl.classList.remove('colab-df-spinner');
          quickchartButtonEl.classList.add('colab-df-quickchart-complete');
        }
        (() => {
          let quickchartButtonEl =
            document.querySelector('#df-e4a4bfca-3d70-4bfa-81b3-5795a3ac32e3 button');
          quickchartButtonEl.style.display =
            google.colab.kernel.accessAllowed ? 'block' : 'none';
        })();
      </script>
    </div>

    </div>
  </div>





```python
path_filename_dict = {i.name: i.as_posix() for i in image_paths}

merged_df['filepath'] = merged_df['file_name'].map(path_filename_dict)
merged_df.head(3)
```





  <div id="df-57325208-a2fc-4f8b-b825-971f2eea693d" class="colab-df-container">
    <div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>license</th>
      <th>file_name</th>
      <th>photographer</th>
      <th>coco_url</th>
      <th>height</th>
      <th>width</th>
      <th>date_captured</th>
      <th>gps_lat_captured</th>
      <th>gps_lon_captured</th>
      <th>flickr_url</th>
      <th>...</th>
      <th>iscrowd</th>
      <th>id_y</th>
      <th>image_id</th>
      <th>category_id</th>
      <th>uuid_y</th>
      <th>individual_ids</th>
      <th>isinterest</th>
      <th>name</th>
      <th>review_ids</th>
      <th>filepath</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>3</td>
      <td>000000000001.jpg</td>
      <td>NNP GZC Car '10WHITE', Person 'A', Image 0005</td>
      <td>None</td>
      <td>2000</td>
      <td>3000</td>
      <td>2015-03-01 14:53:46</td>
      <td>-1.351341</td>
      <td>36.800374</td>
      <td>None</td>
      <td>...</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>7cfac6bc-379a-4859-a5c8-b21b06d2fe3d</td>
      <td>[2, 1, 3, 3459]</td>
      <td>0</td>
      <td>IBEIS_PZ_1561</td>
      <td>[]</td>
      <td>gzgc.coco/images/train2020/000000000001.jpg</td>
    </tr>
    <tr>
      <th>1</th>
      <td>3</td>
      <td>000000000002.jpg</td>
      <td>NNP GZC Car '10WHITE', Person 'A', Image 0006</td>
      <td>None</td>
      <td>2000</td>
      <td>3000</td>
      <td>2015-03-01 14:53:46</td>
      <td>-1.351341</td>
      <td>36.800374</td>
      <td>None</td>
      <td>...</td>
      <td>0</td>
      <td>2</td>
      <td>2</td>
      <td>1</td>
      <td>f56434d5-d829-4b56-a511-6e6c91b2f4fd</td>
      <td>[2, 1, 3, 3459]</td>
      <td>0</td>
      <td>IBEIS_PZ_1561</td>
      <td>[]</td>
      <td>gzgc.coco/images/train2020/000000000002.jpg</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>000000000003.jpg</td>
      <td>NNP GZC Car '10WHITE', Person 'A', Image 0007</td>
      <td>None</td>
      <td>2000</td>
      <td>3000</td>
      <td>2015-03-01 14:53:52</td>
      <td>-1.351341</td>
      <td>36.800374</td>
      <td>None</td>
      <td>...</td>
      <td>0</td>
      <td>3</td>
      <td>3</td>
      <td>1</td>
      <td>34a7063e-2d17-430d-8f9d-ca7199db248b</td>
      <td>[2, 1, 3, 3459]</td>
      <td>0</td>
      <td>IBEIS_PZ_1561</td>
      <td>[]</td>
      <td>gzgc.coco/images/train2020/000000000003.jpg</td>
    </tr>
  </tbody>
</table>
<p>3 rows × 28 columns</p>
</div>
    <div class="colab-df-buttons">

  <div class="colab-df-container">
    <button class="colab-df-convert" onclick="convertToInteractive('df-57325208-a2fc-4f8b-b825-971f2eea693d')"
            title="Convert this dataframe to an interactive table."
            style="display:none;">

  <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960">
    <path d="M120-120v-720h720v720H120Zm60-500h600v-160H180v160Zm220 220h160v-160H400v160Zm0 220h160v-160H400v160ZM180-400h160v-160H180v160Zm440 0h160v-160H620v160ZM180-180h160v-160H180v160Zm440 0h160v-160H620v160Z"/>
  </svg>
    </button>

  <style>
    .colab-df-container {
      display:flex;
      gap: 12px;
    }

    .colab-df-convert {
      background-color: #E8F0FE;
      border: none;
      border-radius: 50%;
      cursor: pointer;
      display: none;
      fill: #1967D2;
      height: 32px;
      padding: 0 0 0 0;
      width: 32px;
    }

    .colab-df-convert:hover {
      background-color: #E2EBFA;
      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);
      fill: #174EA6;
    }

    .colab-df-buttons div {
      margin-bottom: 4px;
    }

    [theme=dark] .colab-df-convert {
      background-color: #3B4455;
      fill: #D2E3FC;
    }

    [theme=dark] .colab-df-convert:hover {
      background-color: #434B5C;
      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);
      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));
      fill: #FFFFFF;
    }
  </style>

    <script>
      const buttonEl =
        document.querySelector('#df-57325208-a2fc-4f8b-b825-971f2eea693d button.colab-df-convert');
      buttonEl.style.display =
        google.colab.kernel.accessAllowed ? 'block' : 'none';

      async function convertToInteractive(key) {
        const element = document.querySelector('#df-57325208-a2fc-4f8b-b825-971f2eea693d');
        const dataTable =
          await google.colab.kernel.invokeFunction('convertToInteractive',
                                                    [key], {});
        if (!dataTable) return;

        const docLinkHtml = 'Like what you see? Visit the ' +
          '<a target="_blank" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'
          + ' to learn more about interactive tables.';
        element.innerHTML = '';
        dataTable['output_type'] = 'display_data';
        await google.colab.output.renderOutput(dataTable, element);
        const docLink = document.createElement('div');
        docLink.innerHTML = docLinkHtml;
        element.appendChild(docLink);
      }
    </script>
  </div>


    <div id="df-389d8970-cddd-4392-b415-29293b255b22">
      <button class="colab-df-quickchart" onclick="quickchart('df-389d8970-cddd-4392-b415-29293b255b22')"
                title="Suggest charts"
                style="display:none;">

<svg xmlns="http://www.w3.org/2000/svg" height="24px"viewBox="0 0 24 24"
     width="24px">
    <g>
        <path d="M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zM9 17H7v-7h2v7zm4 0h-2V7h2v10zm4 0h-2v-4h2v4z"/>
    </g>
</svg>
      </button>

<style>
  .colab-df-quickchart {
      --bg-color: #E8F0FE;
      --fill-color: #1967D2;
      --hover-bg-color: #E2EBFA;
      --hover-fill-color: #174EA6;
      --disabled-fill-color: #AAA;
      --disabled-bg-color: #DDD;
  }

  [theme=dark] .colab-df-quickchart {
      --bg-color: #3B4455;
      --fill-color: #D2E3FC;
      --hover-bg-color: #434B5C;
      --hover-fill-color: #FFFFFF;
      --disabled-bg-color: #3B4455;
      --disabled-fill-color: #666;
  }

  .colab-df-quickchart {
    background-color: var(--bg-color);
    border: none;
    border-radius: 50%;
    cursor: pointer;
    display: none;
    fill: var(--fill-color);
    height: 32px;
    padding: 0;
    width: 32px;
  }

  .colab-df-quickchart:hover {
    background-color: var(--hover-bg-color);
    box-shadow: 0 1px 2px rgba(60, 64, 67, 0.3), 0 1px 3px 1px rgba(60, 64, 67, 0.15);
    fill: var(--button-hover-fill-color);
  }

  .colab-df-quickchart-complete:disabled,
  .colab-df-quickchart-complete:disabled:hover {
    background-color: var(--disabled-bg-color);
    fill: var(--disabled-fill-color);
    box-shadow: none;
  }

  .colab-df-spinner {
    border: 2px solid var(--fill-color);
    border-color: transparent;
    border-bottom-color: var(--fill-color);
    animation:
      spin 1s steps(1) infinite;
  }

  @keyframes spin {
    0% {
      border-color: transparent;
      border-bottom-color: var(--fill-color);
      border-left-color: var(--fill-color);
    }
    20% {
      border-color: transparent;
      border-left-color: var(--fill-color);
      border-top-color: var(--fill-color);
    }
    30% {
      border-color: transparent;
      border-left-color: var(--fill-color);
      border-top-color: var(--fill-color);
      border-right-color: var(--fill-color);
    }
    40% {
      border-color: transparent;
      border-right-color: var(--fill-color);
      border-top-color: var(--fill-color);
    }
    60% {
      border-color: transparent;
      border-right-color: var(--fill-color);
    }
    80% {
      border-color: transparent;
      border-right-color: var(--fill-color);
      border-bottom-color: var(--fill-color);
    }
    90% {
      border-color: transparent;
      border-bottom-color: var(--fill-color);
    }
  }
</style>

      <script>
        async function quickchart(key) {
          const quickchartButtonEl =
            document.querySelector('#' + key + ' button');
          quickchartButtonEl.disabled = true;  // To prevent multiple clicks.
          quickchartButtonEl.classList.add('colab-df-spinner');
          try {
            const charts = await google.colab.kernel.invokeFunction(
                'suggestCharts', [key], {});
          } catch (error) {
            console.error('Error during call to suggestCharts:', error);
          }
          quickchartButtonEl.classList.remove('colab-df-spinner');
          quickchartButtonEl.classList.add('colab-df-quickchart-complete');
        }
        (() => {
          let quickchartButtonEl =
            document.querySelector('#df-389d8970-cddd-4392-b415-29293b255b22 button');
          quickchartButtonEl.style.display =
            google.colab.kernel.accessAllowed ? 'block' : 'none';
        })();
      </script>
    </div>

    </div>
  </div>





```python
merged_df['split'] = merged_df['filepath'].apply(lambda x: Path(x).parent.name)
```


```python
import fiftyone as fo
location = fo.GeoLocation(point=[-73.9855, 40.7580])
```


```python
merged_df.columns
```




    Index(['license', 'file_name', 'photographer', 'coco_url', 'height', 'width',
           'date_captured', 'gps_lat_captured', 'gps_lon_captured', 'flickr_url',
           'id_x', 'uuid_x', 'bbox', 'theta', 'viewpoint', 'segmentation',
           'segmentation_bbox', 'area', 'iscrowd', 'id_y', 'image_id',
           'category_id', 'uuid_y', 'individual_ids', 'isinterest', 'name',
           'review_ids'],
          dtype='object')




```python
# row['gps_lon_captured'], row['gps_lon_captured']

merged_df[['gps_lon_captured', 'gps_lat_captured']] = merged_df[['gps_lon_captured', 'gps_lat_captured']].astype(float)
```


```python
## GZGC Fiftyone Formatting

import fiftyone as fo

samples = []

for _, row in merged_df.head(200).iterrows():
    sample = fo.Sample(
        filepath=row['filepath'],
        split=row['split'],
        identity=row['name'],
        location=fo.GeoLocation(point=[row['gps_lat_captured'], row['gps_lon_captured']])
    )
    samples.append(sample)
```


```python
dataset = fo.Dataset(name='GZGC', overwrite=True)
_ = dataset.add_samples(samples)

```

     100% |█████████████████| 200/200 [156.7ms elapsed, 0s remaining, 1.3K samples/s]  


    INFO:eta.core.utils: 100% |█████████████████| 200/200 [156.7ms elapsed, 0s remaining, 1.3K samples/s]  



```python
map_panel = fo.Panel(type="Map")
```


```python
map_panel
```




    <Panel: {
        'component_id': '947ce174-61f5-42c3-8dbf-ab81d7a41721',
        'type': 'Map',
        'pinned': False,
        'state': {},
    }>




```python
import os
from google.colab import userdata

os.environ['MAPBOX_TOKEN'] = userdata.get('MAPBOX_TOKEN')

```


```python
map_panel_config = {
    "plugins": {
        "map": {
            "mapboxAccessToken": userdata.get('MAPBOX_TOKEN')
        }
    }
}

import os
import json

plug_config_path = "~/.fiftyone/app_config.json"

with open(os.path.expanduser(plug_config_path), 'w') as f:
    json.dump(map_panel_config, f)
```


```python
session = fo.launch_app(dataset, auto=False)
```

    Session launched. Run `session.show()` to open the App in a cell output.


    INFO:fiftyone.core.session.session:Session launched. Run `session.show()` to open the App in a cell output.



```python
dataset.app_config.plugins["map"] = {"mapboxAccessToken": userdata.get('MAPBOX_TOKEN')}
```


```python
session.show()
```



<style>

@import url("https://fonts.googleapis.com/css2?family=Palanquin&display=swap");

body, html {
  margin: 0;
  padding: 0;
  width: 100%;
}

#focontainer-faacf3c0-0d7a-489b-ba49-b7424b2992c3 {
  position: relative;
  height: px;
  display: block !important;
}
#foactivate-faacf3c0-0d7a-489b-ba49-b7424b2992c3 {
  font-weight: bold;
  cursor: pointer;
  font-size: 24px;
  border-radius: 3px;
  text-align: center;
  padding: 0.5em;
  color: rgb(255, 255, 255);
  font-family: "Palanquin", sans-serif;
  position: absolute;
  left: 50%;
  top: 50%;
  width: 160px;
  margin-left: -80px;
  margin-top: -23px;
  background: hsla(210,11%,15%, 0.8);
  border: none;
}
#foactivate-faacf3c0-0d7a-489b-ba49-b7424b2992c3:focus {
  outline: none;
}
#fooverlay-faacf3c0-0d7a-489b-ba49-b7424b2992c3 {
  width: 100%;
  height: 100%;
  background: hsla(208, 7%, 46%, 0.7);
  position: absolute;
  top: 0;
  left: 0;
  display: none;
  cursor: pointer;
}
</style>
<div id="focontainer-faacf3c0-0d7a-489b-ba49-b7424b2992c3" style="display: none;">
   <div id="fooverlay-faacf3c0-0d7a-489b-ba49-b7424b2992c3">
      <button id="foactivate-faacf3c0-0d7a-489b-ba49-b7424b2992c3" >Activate</button>
   </div>
</div>


## Fiftyone Formatting


```python
df['side'] = df['filename'].apply(lambda x: x.split('_')[-1].split('.')[0])
```


```python
import fiftyone as fo

samples = []

for _, row in df.iterrows():
    sample = fo.Sample(
        filepath=row['filepath'],
        split=row['split'],
        identity=row['identity'],
        side = row['side']
    )
    samples.append(sample)
```


```python
dataset = fo.Dataset()
_ = dataset.add_samples(samples)

```

     100% |███████████████| 1942/1942 [814.4ms elapsed, 0s remaining, 2.4K samples/s]      


    INFO:eta.core.utils: 100% |███████████████| 1942/1942 [814.4ms elapsed, 0s remaining, 2.4K samples/s]      



```python
session = fo.launch_app(dataset, auto=False)
```

    Session launched. Run `session.show()` to open the App in a cell output.


    INFO:fiftyone.core.session.session:Session launched. Run `session.show()` to open the App in a cell output.


    
    Welcome to
    
    ███████╗██╗███████╗████████╗██╗   ██╗ ██████╗ ███╗   ██╗███████╗
    ██╔════╝██║██╔════╝╚══██╔══╝╚██╗ ██╔╝██╔═══██╗████╗  ██║██╔════╝
    █████╗  ██║█████╗     ██║    ╚████╔╝ ██║   ██║██╔██╗ ██║█████╗
    ██╔══╝  ██║██╔══╝     ██║     ╚██╔╝  ██║   ██║██║╚██╗██║██╔══╝
    ██║     ██║██║        ██║      ██║   ╚██████╔╝██║ ╚████║███████╗
    ╚═╝     ╚═╝╚═╝        ╚═╝      ╚═╝    ╚═════╝ ╚═╝  ╚═══╝╚══════╝ v1.8.0
    
    If you're finding FiftyOne helpful, here's how you can get involved:
    
    |
    |  ⭐⭐⭐ Give the project a star on GitHub ⭐⭐⭐
    |  https://github.com/voxel51/fiftyone
    |
    |  🚀🚀🚀 Join the FiftyOne Discord community 🚀🚀🚀
    |  https://community.voxel51.com/
    |
    


    INFO:fiftyone.core.session.session:
    Welcome to
    
    ███████╗██╗███████╗████████╗██╗   ██╗ ██████╗ ███╗   ██╗███████╗
    ██╔════╝██║██╔════╝╚══██╔══╝╚██╗ ██╔╝██╔═══██╗████╗  ██║██╔════╝
    █████╗  ██║█████╗     ██║    ╚████╔╝ ██║   ██║██╔██╗ ██║█████╗
    ██╔══╝  ██║██╔══╝     ██║     ╚██╔╝  ██║   ██║██║╚██╗██║██╔══╝
    ██║     ██║██║        ██║      ██║   ╚██████╔╝██║ ╚████║███████╗
    ╚═╝     ╚═╝╚═╝        ╚═╝      ╚═╝    ╚═════╝ ╚═╝  ╚═══╝╚══════╝ v1.8.0
    
    If you're finding FiftyOne helpful, here's how you can get involved:
    
    |
    |  ⭐⭐⭐ Give the project a star on GitHub ⭐⭐⭐
    |  https://github.com/voxel51/fiftyone
    |
    |  🚀🚀🚀 Join the FiftyOne Discord community 🚀🚀🚀
    |  https://community.voxel51.com/
    |
    



```python
session.show()
```



<style>

@import url("https://fonts.googleapis.com/css2?family=Palanquin&display=swap");

body, html {
  margin: 0;
  padding: 0;
  width: 100%;
}

#focontainer-36b42398-d067-4172-a262-a6bc7855b13d {
  position: relative;
  height: px;
  display: block !important;
}
#foactivate-36b42398-d067-4172-a262-a6bc7855b13d {
  font-weight: bold;
  cursor: pointer;
  font-size: 24px;
  border-radius: 3px;
  text-align: center;
  padding: 0.5em;
  color: rgb(255, 255, 255);
  font-family: "Palanquin", sans-serif;
  position: absolute;
  left: 50%;
  top: 50%;
  width: 160px;
  margin-left: -80px;
  margin-top: -23px;
  background: hsla(210,11%,15%, 0.8);
  border: none;
}
#foactivate-36b42398-d067-4172-a262-a6bc7855b13d:focus {
  outline: none;
}
#fooverlay-36b42398-d067-4172-a262-a6bc7855b13d {
  width: 100%;
  height: 100%;
  background: hsla(208, 7%, 46%, 0.7);
  position: absolute;
  top: 0;
  left: 0;
  display: none;
  cursor: pointer;
}
</style>
<div id="focontainer-36b42398-d067-4172-a262-a6bc7855b13d" style="display: none;">
   <div id="fooverlay-36b42398-d067-4172-a262-a6bc7855b13d">
      <button id="foactivate-36b42398-d067-4172-a262-a6bc7855b13d" >Activate</button>
   </div>
</div>


## Assess


```python

```


```python

```


```python

```

## Address


```python

```


```python

```


```python

```
