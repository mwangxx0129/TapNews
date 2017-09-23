import datetime
import hashlib
import redis
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))

import news_api_client # pylint: disable=E0401, C0413
from cloud_amqp_client import CloudAMQPClient # pylint: disable=E0401, C0413

# get config
import config_client # pylint: disable=E0401, C0413
config = config_client.get_config('../config/config_news_pipeline.yaml')
REDIS_HOST = config['news_monitor']['REDIS_HOST']
REDIS_PORT = config['news_monitor']['REDIS_PORT']
SCRAPE_NEWS_TASK_QUEUE_URL = config['news_monitor']['SCRAPE_NEWS_TASK_QUEUE_URL']
SCRAPE_NEWS_TASK_QUEUE_NAME = config['news_monitor']['SCRAPE_NEWS_TASK_QUEUE_NAME']
SLEEP_TIME_IN_SECONDS = 10
NEWS_TIME_OUT_IN_SECONDS = 3600 * 24 * 3

NEWS_SOURCES = [
    'bbc-news',
    'bbc-sport',
    'bloomberg',
    'cnn',
    'entertainment-weekly',
    'espn',
    'ign',
    'techcrunch',
    'the-new-york-times',
    'the-wall-street-journal',
    'the-washington-post'
]

sys.path.append(os.path.join(os.path.dirname(__file__), '..', ''))
from logger.log import LOGGING_NEWS_MONITOR

redis_client = redis.StrictRedis(REDIS_HOST, REDIS_PORT)
cloudAMQP_client = CloudAMQPClient(SCRAPE_NEWS_TASK_QUEUE_URL, SCRAPE_NEWS_TASK_QUEUE_NAME)

while True:
    news_list = news_api_client.getNewsFromSource(NEWS_SOURCES)

    num_of_news_news = 0

    for news in news_list:
        news_digest = hashlib.md5(news['title'].encode('utf-8')).digest().encode('base64')

        if redis_client.get(news_digest) is None:
            num_of_news_news = num_of_news_news + 1
            news['digest'] = news_digest

            if news['publishedAt'] is None:
                news['publishedAt'] = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")

            redis_client.set(news_digest, "True")
            redis_client.expire(news_digest, NEWS_TIME_OUT_IN_SECONDS)

            cloudAMQP_client.send_message(news)
            LOGGING_NEWS_MONITOR.info('[x] Sent message to %s' % (news['title']))

    print "Fetched %d news." % num_of_news_news

    cloudAMQP_client.sleep(SLEEP_TIME_IN_SECONDS)
