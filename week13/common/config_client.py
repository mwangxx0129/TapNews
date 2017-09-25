'''
read config from config/*.yaml
'''
import yaml

# DEFAULT_PATH = '../config/config.yaml'

def get_config(path):
    '''
    get all config
    '''
    with open(path, 'r') as stream:
        try:
            config = yaml.load(stream)
            return config
        except yaml.YAMLError as exc:
            print exc
