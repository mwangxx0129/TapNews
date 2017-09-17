#!/usr/bin/env python
""" config client """

import config_client as client

def test_basic():
    """ test basic """
    monitor_config = client.get_news_monitor_config()
    assert monitor_config['REDIS_HOST'] == 'localhost'
    fecher_config = client.get_news_fecher_config()
    assert fecher_config['SLEEP_TIME_IN_SECONDS'] == 5
    deduper_config = client.get_news_deduper_config()
    assert deduper_config['SLEEP_TIME_IN_SECONDS'] == 1

    print 'test_basic passed.'
    print  monitor_config
    print fecher_config
    print deduper_config

if __name__ == "__main__":
    test_basic()
