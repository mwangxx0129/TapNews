import pyjsonrpc

# get config
import config_client
config = config_client.get_config('../config/config_common.yaml');
URL = config['news_topic_modeling_service_client']['URL']

client = pyjsonrpc.HttpClient(url=URL)

def classify(text):
    topic = client.call('classify', text)
    print "Topic: %s" % str(topic)
    return topic