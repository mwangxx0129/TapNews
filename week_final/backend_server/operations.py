import json
import os
import pickle
import random
import redis
import sys

from bson.json_util import dumps
from datetime import datetime

# import common package in parent directory
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))

import mongodb_client
import news_recommendation_service_client

from cloud_amqp_client import CloudAMQPClient

# get config
import config_client
config = config_client.get_config('../config/config_backend_server.yaml')
REDIS_HOST = config['operations']['REDIS_HOST']
REDIS_PORT = config['operations']['REDIS_PORT']

NEWS_TABLE_NAME = config['operations']['NEWS_TABLE_NAME']
CLICK_LOGS_TABLE_NAME = config['operations']['CLICK_LOGS_TABLE_NAME']

NEWS_LIMIT = config['operations']['NEWS_LIMIT']
NEWS_LIST_BATCH_SIZE = config['operations']['NEWS_LIST_BATCH_SIZE']
USER_NEWS_TIME_OUT_IN_SECONDS = config['operations']['USER_NEWS_TIME_OUT_IN_SECONDS']

LOG_CLICKS_TASK_QUEUE_URL = "amqp://hwobvzoo:bRJDd0L2vyglauta1fFbsGjfcwyAmVWa@donkey.rmq.cloudamqp.com/hwobvzoo"
LOG_CLICKS_TASK_QUEUE_NAME = "tap-news-log-clicks-task-queue"

redis_client = redis.StrictRedis(REDIS_HOST, REDIS_PORT, db=0)
cloudAMQP_client = CloudAMQPClient(LOG_CLICKS_TASK_QUEUE_URL, LOG_CLICKS_TASK_QUEUE_NAME)

def getNewsSummariesForUser(user_id, page_num):
    page_num = int(page_num)
    begin_index = (page_num - 1) * NEWS_LIST_BATCH_SIZE
    end_index = page_num * NEWS_LIST_BATCH_SIZE

    # The final list of news to be returned.
    sliced_news = []
    print 'getNewsSummariesForUser'
    
    if redis_client.get(user_id) is not None:
        news_digests = pickle.loads(redis_client.get(user_id))

        # If begin_index is out of range, this will return empty list;
        # If end_index is out of range (begin_index is within the range), this
        # will return all remaining news ids.
        sliced_news_digests = news_digests[begin_index:end_index]
        print sliced_news_digests
        db = mongodb_client.get_db()
        sliced_news = list(db[NEWS_TABLE_NAME].find({'digest':{'$in':sliced_news_digests}}))
    else:
        db = mongodb_client.get_db()
        total_news = list(db[NEWS_TABLE_NAME].find().sort([('publishedAt', -1)]).limit(NEWS_LIMIT))
        total_news_digests = map(lambda x:x['digest'], total_news)

        redis_client.set(user_id, pickle.dumps(total_news_digests))
        redis_client.expire(user_id, USER_NEWS_TIME_OUT_IN_SECONDS)

        sliced_news = total_news[begin_index:end_index]

    # Get preference for the user
    preference = news_recommendation_service_client.getPreferenceForUser(user_id)
    topPreference = None

    if preference is not None and len(preference) > 0:
        topPreference = preference[0]

    for news in sliced_news:
        # Remove text field to save bandwidth.
        del news['text']
        if news['class'] == topPreference:
            news['reason'] = 'Recommend'
        if news['publishedAt'].date() == datetime.today().date():
            news['time'] = 'today'
    return json.loads(dumps(sliced_news))


def logNewsClickForUser(user_id, news_id):
    print '[logNewsClickForUser]\n'
    # print 'user_id ', user_id
    # print 'news_id', news_id
    message = {'userId': user_id, 'newsId': news_id, 'timestamp': datetime.utcnow()}

    db = mongodb_client.get_db()
    # save all log
    db[CLICK_LOGS_TABLE_NAME].insert(message)
    
    # save daily log
    day_click_logs_table_name = CLICK_LOGS_TABLE_NAME + datetime.today().strftime('_%Y-%m-%d')
    print 'table: ' + day_click_logs_table_name
    db[day_click_logs_table_name].insert(message)

    # count clickinng number evey hour
    update_hour_clicking_number()

    # update user freq
    update_daily_active_users_freq(user_id)

    # update item freq
    update_daily_active_news_freq(news_id)

    # update_daily_active_users
    update_daily_active_users(user_id)

    # Send log task to machine learning service for prediction
    message = {'userId': user_id, 'newsId': news_id, 'timestamp': str(datetime.utcnow())}
    cloudAMQP_client.send_message(message)

DEFAULT_DAY_FORMAT = '%Y-%m-%d' + '_'
DEFAULT_HOUR_FORMAT = '%Y-%m-%d-%H' + '_'
DEFAULT_EXPIRE_SECONDS = 60 * 60

HOUR_CLICKING_NUMBER = 'hour_clicking_number' + '_'

DAILY_ACTIVE_USERS = 'daily_active_users' + '_'
DAILY_ACTIVE_USERS_FREQ = 'daily_active_users_freq' + '_'
DAILY_ACTIVE_NEWS_FREQ = 'daily_active_news_freq' + '_'



def addOne(key, expire_seconds=DEFAULT_EXPIRE_SECONDS):
    '''
    common add one on given key
    '''

    if redis_client.get(key) is None:
        count = 0
    else:
        count = int(redis_client.get(key))
    redis_client.set(key, count + 1)
    redis_client.expire(key, expire_seconds)
    # print 'key: ' + key + '\tval: ' + count + 1

def update_hour_clicking_number():
    '''
    total clicking number per hour
    '''
    hour = datetime.today().strftime(DEFAULT_HOUR_FORMAT)
    key = HOUR_CLICKING_NUMBER + hour
    print key
    addOne(key)
    

def update_daily_active_users_freq(user_id):
    print 'update_daily_active_users_freq'
    day = datetime.today().strftime(DEFAULT_DAY_FORMAT)
    key = DAILY_ACTIVE_USERS_FREQ + day + user_id
    addOne(key)

def update_daily_active_news_freq(news_id):
    print 'update_daily_active_news_freq'
    day = datetime.today().strftime(DEFAULT_DAY_FORMAT)
    key = DAILY_ACTIVE_NEWS_FREQ + day + news_id
    addOne(key, 60 * 60 * 24)

def update_daily_active_users(user_id):
    '''
    if user is NOT exist in daily_active_users_freq, add one
    '''
    print 'update_daily_active_users'
    day = datetime.today().strftime(DEFAULT_DAY_FORMAT)

    # daily_active_users_frq 
    daily_active_users_frq = DAILY_ACTIVE_USERS_FREQ + day + user_id
    
    key = DAILY_ACTIVE_USERS + day

    # if user_id is not in active 
    if redis_client.get(daily_active_users_frq) is None:
        addOne(key)
