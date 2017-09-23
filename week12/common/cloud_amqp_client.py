""" Cloud AMQP Client """

import json
import pika

import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..', ''))
from logger.log import LOGGING_OHTER

class CloudAMQPClient(object):
    """ Cloud AMQP Client """
    def __init__(self, cloud_amqp_url, queue_name):
        self.cloud_amqp_url = cloud_amqp_url
        self.queue_name = queue_name
        self.params = pika.URLParameters(cloud_amqp_url)
        self.params.socket_time_timeout = 3
        self.connection = pika.BlockingConnection(self.params)
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue=queue_name)

    # send a message
    def send_message(self, message):
        '''send a message'''
        self.channel.basic_publish(exchange='',
                                   routing_key=self.queue_name,
                                   body=json.dumps(message))
        # LOGGING_OHTER.info('[x] Sent message to %s: %s' % (self.queue_name, message))
        # print '[x] Sent message to %s: %s' % (self.queue_name, message)

    # get a message
    def get_message(self):
        ''' get a message '''
        method_frame, header_frame, body = self.channel.basic_get(self.queue_name)
        if method_frame:
            # LOGGING_OHTER.info('[x] Sent message to %s: %s' % (self.queue_name, body))
            # print '[x] Received message from %s: %s' % (self.queue_name, body)
            self.channel.basic_ack(method_frame.delivery_tag)
            return json.loads(body)
        else:
            print 'No message returned.'
            return None

    # BlockingConnection.sleep is a safer way to sleep than time.sleep().
    def sleep(self, seconds):
        ''' sleep for safe '''
        self.connection.sleep(seconds)
