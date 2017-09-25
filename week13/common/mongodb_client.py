#!/usr/bin/env python
""" Mongo Client """
from pymongo import MongoClient

# get config
import config_client
config = config_client.get_config('../config/config_common.yaml');
MONGO_DB_HOST = config['mongodb_client']['MONGO_DB_HOST']
MONGO_DB_PORT = config['mongodb_client']['MONGO_DB_PORT']
DB_NAME = config['mongodb_client']['DB_NAME']

CLIENT = MongoClient("%s:%s" % (MONGO_DB_HOST, MONGO_DB_PORT))

def get_db(db_name=DB_NAME):
    ''' get db with name of db'''
    return CLIENT[db_name]
