import json
from bson.json_util import dumps

import redis
# from datetime import datetime

from datetime import datetime, timedelta

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

    print key
    if redis_client.get(key) is None:
        count = 0
    else:
        count = redis_client.get(key)
    return count

def get_daily_active_time():
    '''
    {
        "2017-09-30:00" : "200"
        "2017-09-30:01" : "300"
        ...
        "2017-09-30:23" : "200"
    }
    '''
    
    return




