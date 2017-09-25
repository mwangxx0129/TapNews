import pyjsonrpc


# get config
import config_client
config = config_client.get_config('../config/config_common.yaml');
URL = config['news_recommendation_service_client']['URL']

client = pyjsonrpc.HttpClient(url=URL)

def getPreferenceForUser(userId):
    preference = client.call('getPreferenceForUser',userId)
    print "Preference list: %s" % str(preference)
    return preference

