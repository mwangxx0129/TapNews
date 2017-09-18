#!/usr/bin/env python
""" mongodb client """

import mongodb_client as client

def test_basic():
    """ test basic """
    db_name = client.get_db('test')
    db_name.testCollection.drop()
    assert db_name.testCollection.count() == 0
    db_name.testCollection.insert({'test': 1, 'hello': 'world'})
    assert db_name.testCollection.count() == 1
    db_name.testCollection.drop()
    assert db_name.testCollection.count() == 0
    print 'test_basic passed.'

if __name__ == "__main__":
    test_basic()
