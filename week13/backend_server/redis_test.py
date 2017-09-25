import redis

REDIS_HOST = 'localhost'
REDIS_PORT = '6379'

redis_client = redis.StrictRedis(REDIS_HOST, REDIS_PORT, db=0)

redis_client.set('demo', 1)
count = int(redis_client.get('demo')) + 1

key = 'user_id' + '_freq'
if (redis_client.get(key) is None):
    count = 0
else:
    count = redis_client.get(key)

print key, count + 1
redis_client.set(key, count + 1)

print count