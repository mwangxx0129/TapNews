import os
import sys

from newspaper import Article

# import common package in parent directory
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))
sys.path.append(os.path.join(os.path.dirname(__file__), 'scrapers'))

import cnn_news_scraper
from cloud_amqp_client import CloudAMQPClient

# TODO: use your own queue.

SCRAPE_NEWS_TASK_QUEUE_URL = 'amqp://xpiykasc:6iOMy4O0EA0vRjaA7KmUpt_m02onHG2f@donkey.rmq.cloudamqp.com/xpiykasc'
SCRAPE_NEWS_TASK_QUEUE_NAME = 'tap-news-scrape-news-task-queue'

DEDUPE_NEWS_TASK_QUEUE_URL = 'amqp://xqwzopki:8Y2BfWh2p2-Wvyd7tXfnq2q90CnB48C3@donkey.rmq.cloudamqp.com/xqwzopki'
DEDUPE_NEWS_TASK_QUEUE_NAME = 'tap-news-dedupe-news-task-queue'

SLEEP_TIME_IN_SECONDS = 5

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
