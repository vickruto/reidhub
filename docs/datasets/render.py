from pathlib import Path
import yaml
from jinja2 import Environment, FileSystemLoader

# Get the absolute path of the directory containing this script
BASE_DIR = Path(__file__).resolve().parent

## CONFIG
# YAML_ROOT = BASE_DIR / 'cfg'
# OUTPUTS_ROOT = BASE_DIR 
# OVERVIEWS_ROOT = BASE_DIR / 'overviews'
# CITATIONS_ROOT = BASE_DIR / 'citations'
# NOTES_ROOT = BASE_DIR / 'notes'
# template_path = BASE_DIR / 'template.md.jinja'

## CONFIG
YAML_ROOT = Path('cfg')
OUTPUTS_ROOT = Path()
OVERVIEWS_ROOT = Path('overviews')
CITATIONS_ROOT = Path('citations')
NOTES_ROOT = Path('notes')


# datasets_list = ['gzgc']
datasets_list = (BASE_DIR/"cfg").glob('*.yaml')

for yaml_config_path in datasets_list:
    dataset_slug = yaml_config_path.stem
    output_readme_path = BASE_DIR / f'{dataset_slug}.md'
    overview_path = Path('overviews') / f'overview-{dataset_slug}.md'
    citation_path = Path('citations') / f'citation-{dataset_slug}.md'
    notes_path = Path('notes') / f'notes-{dataset_slug}.md'

    # Load YAML config
    with open(yaml_config_path) as f:
        dataset_info = yaml.safe_load(f)
    dataset_info['overview_path'] = str(overview_path)
    dataset_info['citation_path'] = str(citation_path)
    dataset_info['notes_path'] = str(notes_path)

    # Setup Jinja environment
    env = Environment(loader=FileSystemLoader(searchpath=BASE_DIR))

    # Load template
    template = env.get_template('template.md.jinja')

    # Render
    output = template.render(**dataset_info)

    # Save
    with open(output_readme_path, "w") as f:
        f.write(output)

    print(f"Rendered {output_readme_path} ✅")
