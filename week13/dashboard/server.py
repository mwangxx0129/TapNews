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

@app.route("/devices")
def devices():
    data = {
        "android" : "300",
        "iPhone6s": "200",
        "pc" : "20"
    }
    response = app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )
    return response

if __name__ == "__main__":
    app.run()