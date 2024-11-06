import yaml

#Load Yaml Config
def load_config(config_path):

    with open(config_path, 'r') as config_yaml:
        config = yaml.safe_load(config_yaml)
    return config
