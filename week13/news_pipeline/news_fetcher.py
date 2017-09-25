import os
import sys

from newspaper import Article

# import common package in parent directory
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))
sys.path.append(os.path.join(os.path.dirname(__file__), 'scrapers'))

import cnn_news_scraper
from cloud_amqp_client import CloudAMQPClient

# get config
import config_client
config = config_client.get_config('../config/config_news_pipeline.yaml')
SCRAPE_NEWS_TASK_QUEUE_URL = config['news_fetcher']['SCRAPE_NEWS_TASK_QUEUE_URL']
SCRAPE_NEWS_TASK_QUEUE_NAME = config['news_fetcher']['SCRAPE_NEWS_TASK_QUEUE_NAME']
DEDUPE_NEWS_TASK_QUEUE_URL = config['news_fetcher']['DEDUPE_NEWS_TASK_QUEUE_URL']
DEDUPE_NEWS_TASK_QUEUE_NAME = config['news_fetcher']['DEDUPE_NEWS_TASK_QUEUE_NAME']
SLEEP_TIME_IN_SECONDS = config['news_fetcher']['SLEEP_TIME_IN_SECONDS']

# log
sys.path.append(os.path.join(os.path.dirname(__file__), '..', ''))
from logger.log import LOGGING_NEWS_FETCHER

dedupe_news_queue_client = CloudAMQPClient(DEDUPE_NEWS_TASK_QUEUE_URL, DEDUPE_NEWS_TASK_QUEUE_NAME)
scrape_news_queue_client = CloudAMQPClient(SCRAPE_NEWS_TASK_QUEUE_URL, SCRAPE_NEWS_TASK_QUEUE_NAME)

def handle_message(msg):
    if msg is None or not isinstance(msg, dict):
        print 'message is broken'
        return

    task = msg
    text = None
    
    article = Article(task['url'])
    article.download()
    article.parse()

    task['text'] = article.text.encode('utf-8')
    LOGGING_NEWS_FETCHER.info('[x] Fetcher message to %s' % (msg['title']))
    dedupe_news_queue_client.send_message(task)

while True:
    if scrape_news_queue_client is not None:
        msg = scrape_news_queue_client.get_message()
        if msg is not None:
            try:
                handle_message(msg)
            except Exception as e:
                print # coding=utf-8
                pass
        scrape_news_queue_client.sleep(SLEEP_TIME_IN_SECONDS)
