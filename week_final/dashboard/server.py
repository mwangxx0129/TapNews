import operations
import json
from flask import Flask
app = Flask(__name__)
 
@app.route("/")
def index():
    return "Index!"
 
@app.route("/hello")
def hello():
    return "Hello World!"
 
@app.route("/members")
def members():
    return "Members"
 
@app.route("/members/<string:name>/")
def getMember(name):
    return name

@app.route("/hourClickingNumber")
def get_hour_clicking_number():
    # return "hour_clicking_number"
    data = operations.get_hour_clicking_number()
    response = app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )
    return response

@app.route("/hourClickingNumberParam/<string:delta>/")
def get_hour_clicking_number_param(delta):
    count = operations.get_hour_clicking_number(int(delta))
    data = {
        "hour_clicking_number": count
    }
    response = app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )
    return response

# API userStatisticsData
@app.route("/userStatisticsData")
def user_statistics_data():
    data = [
        {
            'title': 'Total Users',
            'num':operations.totalUsers()
        },
        {
            'title': 'New Users (Today)',
            'num':23
        },
        {
            'title': 'Active Users (Today)',
            'num':operations.dailyActiveUsers()
        },
        {
            'title': 'Average Usage Time',
            'num':12
        }
    ]
    response = app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )
    return response

# API userTrend
@app.route("/userTrend")
def userTrend():
    data = [
        {
            'name': 'New User',
            'data': [20, 50, 34, 20, 90,74, 110]
        },
        {
            'name': 'Active User',
            'data': operations.get_previous_week_users()
        }
    ]
    response = app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )
    return response

# API userDevice
# Done
@app.route("/userDevice")
def userDevice():
    ios = operations.get_device('IOS')
    android = operations.get_device('Android')
    mac = operations.get_device('MAC')
    windows = operations.get_device('Windows')
    pad = operations.get_device('Pad')
    other = operations.get_device('other')

    total = ios + android + mac + windows + pad + other
    total = total * 1.0

    data = [
        {
            'name': 'IOS',
            'y': ios,
        }, {
            'name': 'Android',
            'y': android,
        }, {
            'name': 'MAC',
            'y': mac,
        }, {
            'name': 'Windows',
            'y': windows,
        }, {
            'name': 'Pad',
            'y': pad,
        }, {
            'name': 'other',
            'y': other
        }
    ]
    # remove it 
    print data
    response = app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )
    return response

# API newsCategory
# TODO
@app.route("/newsCategory")
def newsCategory():
    data = [
        {
            'name': 'technology',
            'y': operations.get_news_category('technology')
        },
        {
            'name': 'world',
            'y': operations.get_news_category('world')
        },
        {
            'name': 'education',
            'y': operations.get_news_category('education')
        },
        {
            'name': 'sports',
            'y': operations.get_news_category('sports')
        },
        {
            'name': 'weather',
            'y': operations.get_news_category('weather')
        },
    ]
    response = app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )
    return response

# API User Active Time Distribution(24 hours)
# Done
@app.route("/userActiveTimeDistribution")
def userActiveTimeDistribution():
    data = [
            {
                'name': 'Operation Number',
                'data': operations.get_daily_active_time()
            }
    ]
    response = app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )
    return response

if __name__ == "__main__":
    app.run()