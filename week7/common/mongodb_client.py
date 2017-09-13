#!/usr/bin/env python
""" Mongo Client """
from pymongo import MongoClient

MONGO_DB_HOST = 'localhost'
MONGO_DB_PORT = '27017'
DB_NAME = 'tap-news'

CLIENT = MongoClient("%s:%s" % (MONGO_DB_HOST, MONGO_DB_PORT))

def get_db(db_name=DB_NAME):
    ''' get db with name of db'''
    return CLIENT[db_name]
