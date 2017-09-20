'''
req to NewsAPI
extract info from res
populate source
'''
from json import loads
import requests

# get config
import config_client
config = config_client.get_config('../config/config_common.yaml');
NEWS_API_ENDPOINT = config['news_api_client']['NEWS_API_ENDPOINT']
NEWS_API_KEY = config['news_api_client']['NEWS_API_KEY']
ARTICLES_API = config['news_api_client']['ARTICLES_API']
SORT_BY_TOP = config['news_api_client']['SORT_BY_TOP']

BBC_NEWS = 'bbc-news'
BBC_SPORT = 'bbc-sport'
CNN = 'cnn'

DEFAULT_SOURCES = [BBC_NEWS, CNN]


def build_url(end_point=NEWS_API_ENDPOINT, api_name=ARTICLES_API):
    '''
    get url
    '''
    return end_point + api_name

def getNewsFromSource(sources=DEFAULT_SOURCES, sort_by=SORT_BY_TOP):
    articles = []

    for source in sources:
        payload = {'apiKey':NEWS_API_KEY,
                   'source':source,
                   'sortBy':sort_by}

        response = requests.get(build_url(), params=payload)

        print response.content
        res_json = loads(response.content)

        # Extract info from response
        if (res_json is not None and 
            res_json['status'] == 'ok' and 
            res_json['source'] is not None):
            # populate news source in each articles
            for news in res_json['articles']:
                news['source'] = res_json['source']

            articles.extend(res_json['articles'])

    return articles
