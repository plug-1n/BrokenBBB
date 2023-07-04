import yaml
import sys

def get_config_yaml(name:str='config.yaml')->dict:
    try:
        with open(name, "r") as stream:
            config_data = yaml.safe_load(stream)
    except (FileNotFoundError,yaml.YAMLError)  as err:  
        sys.exit(err)     
    return config_data.values()