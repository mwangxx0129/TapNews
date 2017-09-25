import os
import sys

# import common package in parent directory
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))

import mongodb_client
import news_topic_modeling_service_client

import config_client
config = config_client.get_config('../config/config_machine_learning_server.yaml')

NEWS_TABLE_NAME = config['mongodb_client']['NEWS_TABLE_NAME']

if __name__ == '__main__':
    db = mongodb_client.get_db()
    cursor = db[NEWS_TABLE_NAME].find({})
    count = 0
    for news in cursor:
        count += 1
        print count
        if 'class' not in news:
            print 'Populating classes...'
            description = news['description']
            if description is None:
                description = news['title']

            topic = news_topic_modeling_service_client.classify(description)
            news['class'] = topic
            db[NEWS_TABLE_NAME].replace_one({'digest': news['digest']}, news, upsert=True)
