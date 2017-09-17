'''
read config from config/*.yaml
'''
import yaml

DEFAULT_PATH = '../config/news_pipeline.yaml'

def get_news_all_config(path=DEFAULT_PATH):
    '''
    get all config
    '''
    with open(path, 'r') as stream:
        try:
            config = yaml.load(stream)
            return config
        except yaml.YAMLError as exc:
            print exc

def get_news_monitor_config(path=DEFAULT_PATH):
    '''
    get config of monitor
    '''
    return get_news_all_config(path)['news_monitor']

def get_news_fecher_config(path=DEFAULT_PATH):
    '''
    get config of fecher
    '''
    return get_news_all_config(path)['news_fecher']

def get_news_deduper_config(path=DEFAULT_PATH):
    '''
    get config of deduper
    '''
    return get_news_all_config(path)['news_deduper']
