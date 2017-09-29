import redis
from datetime import datetime

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



def get_hour_clicking_number():
    '''
    get the number of clicking every hour
    '''
    hour = datetime.today().strftime(DEFAULT_HOUR_FORMAT)
    key = CLICKING_NUMBER_PER_HOUR + hour
    if redis_client.get(key) is None:
        count = -1
    else:
        count = int(redis_client.get(key))
    return count

def get_daily_active_users():
    '''
    get the number of daily active user
    '''
    return




