""" cloudamqp client test"""

from cloud_amqp_client import CloudAMQPClient


CLOUDAMQP_URL = 'amqp://xqwzopki:8Y2BfWh2p2-Wvyd7tXfnq2q90CnB48C3@donkey.rmq.cloudamqp.com/xqwzopki'
TEST_QUEUE_NAME = 'tap-news-scrape-news-task-queue'

def test_basic():
    """ test_basic"""
    client = CloudAMQPClient(CLOUDAMQP_URL, TEST_QUEUE_NAME)

    sent_msg = {'test': 'test'}
    client.send_message(sent_msg)
    received_msg = client.get_message()

    assert sent_msg == received_msg
    print 'test_basic passed.'

if __name__ == '__main__':
    test_basic()