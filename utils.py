import yaml
from box import ConfigBox

def read_yaml(path):
    with open(path) as file:
        content=yaml.safe_load(file)
        return ConfigBox(content)