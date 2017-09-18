'''
req to NewsAPI
extract info from res
populate source
'''
from json import loads
import requests

NEWS_API_ENDPOINT = 'https://newsapi.org/v1/'
NEWS_API_KEY = 'c6782a51efc748129f5a47e273fe9aac'

ARTICLES_API = 'articles'

BBC_NEWS = 'bbc-news'
BBC_SPORT = 'bbc-sport'
CNN = 'cnn'

DEFAULT_SOURCES = [BBC_NEWS, CNN]
SORT_BY_TOP = 'top'

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
