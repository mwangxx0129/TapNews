import operator
import os
import pyjsonrpc
import sys

# import common package in parent directory
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))

import mongodb_client

# get config
import config_client
config = config_client.get_config('../config/config_news_recommendation_service.yaml')
PREFERENCE_MODEL_TABLE_NAME = config['click_log_processor']['PREFERENCE_MODEL_TABLE_NAME']

SERVER_HOST = config['service']['SERVER_HOST']
SERVER_PORT = config['service']['SERVER_PORT']

# Ref: https://www.python.org/dev/peps/pep-0485/#proposed-implementation
# Ref: http://stackoverflow.com/questions/5595425/what-is-the-best-way-to-compare-floats-for-almost-equality-in-python
def isclose(a, b, rel_tol=1e-09, abs_tol=0.0):
    return abs(a-b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol)

class RequestHandler(pyjsonrpc.HttpRequestHandler):
    """ Get user's preference in an ordered class list """
    @pyjsonrpc.rpcmethod
    def getPreferenceForUser(self, user_id):
        db = mongodb_client.get_db()
        model = db[PREFERENCE_MODEL_TABLE_NAME].find_one({'userId':user_id})
        if model is None:
            return []

        sorted_tuples = sorted(model['preference'].items(), key=operator.itemgetter(1), reverse=True)
        sorted_list = [x[0] for x in sorted_tuples]
        sorted_value_list = [x[1] for x in sorted_tuples]

        # If the first preference is same as the last one, the preference makes
        # no sense.
        if isclose(float(sorted_value_list[0]), float(sorted_value_list[-1])):
            return []

        return sorted_list


# Threading HTTP Server
http_server = pyjsonrpc.ThreadingHttpServer(
    server_address = (SERVER_HOST, SERVER_PORT),
    RequestHandlerClass = RequestHandler
)

print "Starting HTTP server on %s:%d" % (SERVER_HOST, SERVER_PORT)

http_server.serve_forever()