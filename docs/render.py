from pathlib import Path
import yaml
from jinja2 import Environment, FileSystemLoader

## CONFIG
YAML_ROOT = Path('dataset-stats')
TEMPLATES_ROOT = Path('templates')
OUTPUTS_ROOT = Path('output-dataset-readmes')
OVERVIEWS_ROOT = Path('overviews') 
CITATIONS_ROOT = Path('citations') 

OUTPUTS_ROOT.mkdir(parents=True, exist_ok=True)

datasets_list = ['gzgc']
for dataset in datasets_list:
    yaml_config_path =  YAML_ROOT / f'stats-{dataset}.yaml' 
    template_path = TEMPLATES_ROOT / f'template-{dataset}.md.jinja'
    output_readme_path = OUTPUTS_ROOT / f'{dataset}.md'
    overview_path = OVERVIEWS_ROOT / f'overview-{dataset}.md'
    citation_path = CITATIONS_ROOT / f'citation-{dataset}.md'

    # Load YAML config
    with open(yaml_config_path) as f:
        dataset_info = yaml.safe_load(f)
    dataset_info['overview_path'] = str(overview_path)
    dataset_info['citation_path'] = str(citation_path)

    # Setup Jinja environment
    env = Environment(loader=FileSystemLoader("."))

    # Load template
    template = env.get_template(str(template_path))

    # Render
    output = template.render(**dataset_info)

    # Save
    with open(output_readme_path, "w") as f:
        f.write(output)

    print(f"Rendered {output_readme_path} ✅")
