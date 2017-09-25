'''
test LOGGING module
'''
# import common package in parent directory
# sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'logger'))

# from log import parser, crawler, storage
from log import LOGGING_NEWS_MONITOR, LOGGING_NEWS_FETCHER
from log import LOGGING_NEWS_DEDUPER, LOGGING_OHTER

LOGGING_NEWS_MONITOR.info('This is crawler')

LOGGING_NEWS_FETCHER.info('This is info')

LOGGING_NEWS_DEDUPER.info('tihs is error')

LOGGING_OHTER.info('tihs is error')
