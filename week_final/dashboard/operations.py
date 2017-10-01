import os
import sys
import json
from bson.json_util import dumps
import redis
# from datetime import datetime
from datetime import datetime, timedelta
# import common package in parent directory
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))

import mongodb_client  # pylint: disable=E0401, C0413



DEFAULT_REDIS_HOST = 'localhost'
DEFAULT_REDIS_PORT = '6379'

REDIS_HOST = DEFAULT_REDIS_HOST
REDIS_PORT = DEFAULT_REDIS_PORT

redis_client = redis.StrictRedis(REDIS_HOST, REDIS_PORT, db=0)


DEFAULT_DAY_FORMAT = '%Y-%m-%d' + '_'
DEFAULT_HOUR_FORMAT = '%Y-%m-%d-%H' + '_'
DEFAULT_EXPIRE_SECONDS = 60 * 60

HOUR_CLICKING_NUMBER = 'hour_clicking_number' + '_'

DAILY_ACTIVE_USERS = 'daily_active_users' + '_'
DAILY_ACTIVE_USERS_FREQ = 'daily_active_users_freq' + '_'
DAILY_ACTIVE_NEWS_FREQ = 'daily_active_news_freq' + '_'



db = mongodb_client.get_db()

def getValue(key):
    if redis_client.get(key) is None:
        count = 0
    else:
        count = redis_client.get(key)
    return count

def totalUsers():
    return db["users"].find().count()

def dailyActiveUsers():
    day = datetime.today().strftime(DEFAULT_DAY_FORMAT)
    key = DAILY_ACTIVE_USERS + day
    return getValue(key)

def get_hour_clicking_number(time_delta=0):
    '''
    get the number of clicking every hour
    200
    '''
    print "operations/get_hour_clicking_number"

    # get previous hour time
    # hour = datetime.today().strftime(DEFAULT_HOUR_FORMAT)
    lastHourDateTime = datetime.today() - timedelta(hours = time_delta)

    # format %Y-%m-%d-%H
    hour = lastHourDateTime.strftime(DEFAULT_HOUR_FORMAT)

    # get key
    key = HOUR_CLICKING_NUMBER + hour

    return getValue(key)

def get_daily_active_time():
    res = []
    # get current hour
    curHour = datetime.today().hour

    for i in range(curHour):
        res.insert(0, get_hour_clicking_number(i))
    
    return res

def get_daily_active_users(time_delta=0):
    # get previous hour time
    # hour = datetime.today().strftime(DEFAULT_HOUR_FORMAT)
    lastDayDateTime = datetime.today() - timedelta(days = time_delta)

    day = lastDayDateTime.strftime(DEFAULT_DAY_FORMAT)
    key = DAILY_ACTIVE_USERS + day
    return getValue(key)

def get_previous_week_users():
    res = []
    # get current hour
    for i in range(7):
        res.insert(0, get_daily_active_users(i))
    return res

# TODO config
devices = [
    "IOS",
    "Android",
    "MAC",
    "Windows",
    "Pad",
    "other"
]

def get_device(device):
    return getValue(device.lower())

def get_news_category(news_category):
    return getValue(news_category.lower())
