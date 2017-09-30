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
def userStatisticsData():
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
            'data': [74, 110,50, 34, 20, 90,74]
        }
    ]
    response = app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )
    return response

# API userDevice
@app.route("/userDevice")
def userDevice():
    data = [
        {
            'name': 'IOS',
            'y': 56.33,
        }, {
            'name': 'Android',
            'y': 24.03,
        }, {
            'name': 'MAC',
            'y': 10.38,
        }, {
            'name': 'Windows',
            'y': 4.77,
        }, {
            'name': 'Pad',
            'y': 0.91,
        }, {
            'name': 'other',
            'y': 2
        }
    ]
    response = app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )
    return response

# API newsCategory
@app.route("/newsCategory")
def newsCategory():
    data = [
        {
            'name': 'technology',
            'y': 50
        },
        {
            'name': 'music',
            'y': 150
        },
        {
            'name': 'education',
            'y': 30
        },
        {
            'name': 'sports',
            'y': 50
        },
        {
            'name': 'weather',
            'y': 50
        },
    ]
    response = app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )
    return response

# API User Active Time Distribution(24 hours)
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