import os
import sys
# import yaml

# import common package in parent directory
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))

# import news_api_client  # pylint: disable=E0401, C0413
from cloud_amqp_client import CloudAMQPClient # pylint: disable=E0401, C0413

# TODO: use your own queue.

SCRAPE_NEWS_TASK_QUEUE_URL_o = 'amqp://xpiykasc:6iOMy4O0EA0vRjaA7KmUpt_m02onHG2f@donkey.rmq.cloudamqp.com/xpiykasc'
SCRAPE_NEWS_TASK_QUEUE_NAME_o = 'tap-news-scrape-news-task-queue'

DEDUPE_NEWS_TASK_QUEUE_URL_o = 'amqp://xqwzopki:8Y2BfWh2p2-Wvyd7tXfnq2q90CnB48C3@donkey.rmq.cloudamqp.com/xqwzopki'
DEDUPE_NEWS_TASK_QUEUE_NAME_o = 'tap-news-dedupe-news-task-queue'

# get config
import config_client
config = config_client.get_config('../config/config_news_pipeline.yaml')
# REDIS_HOST = config['news_monitor']['REDIS_HOST']
# REDIS_PORT = config['news_monitor']['REDIS_PORT']
SCRAPE_NEWS_TASK_QUEUE_URL = config['news_fetcher']['SCRAPE_NEWS_TASK_QUEUE_URL']
SCRAPE_NEWS_TASK_QUEUE_NAME = config['news_fetcher']['SCRAPE_NEWS_TASK_QUEUE_NAME']

DEDUPE_NEWS_TASK_QUEUE_URL = config['news_fetcher']['DEDUPE_NEWS_TASK_QUEUE_URL']
DEDUPE_NEWS_TASK_QUEUE_NAME = config['news_fetcher']['DEDUPE_NEWS_TASK_QUEUE_NAME']

def clear_queue(queue_url, queue_name):
    '''clearQueue'''
    scrape_news_queue_client = CloudAMQPClient(queue_url, queue_name)

    num_of_messages = 0

    while True:
        if scrape_news_queue_client is not None:
            msg = scrape_news_queue_client.get_message()
            if msg is None:
                print "Cleared %d messages." % num_of_messages
                return
            num_of_messages += 1


if __name__ == "__main__":
    # print SCRAPE_NEWS_TASK_QUEUE_URL
    # print SCRAPE_NEWS_TASK_QUEUE_URL_o == SCRAPE_NEWS_TASK_QUEUE_URL
    # print SCRAPE_NEWS_TASK_QUEUE_NAME_o == SCRAPE_NEWS_TASK_QUEUE_NAME
    # print DEDUPE_NEWS_TASK_QUEUE_URL_o == DEDUPE_NEWS_TASK_QUEUE_URL
    # print DEDUPE_NEWS_TASK_QUEUE_NAME_o == DEDUPE_NEWS_TASK_QUEUE_NAME
    clear_queue(SCRAPE_NEWS_TASK_QUEUE_URL, SCRAPE_NEWS_TASK_QUEUE_NAME)
    clear_queue(DEDUPE_NEWS_TASK_QUEUE_URL, DEDUPE_NEWS_TASK_QUEUE_NAME)
