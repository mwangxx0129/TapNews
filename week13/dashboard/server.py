import operations
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

@app.route("/active_user/")
def get_hour_clicking_number():
    return get_hour_clicking_number()

if __name__ == "__main__":
    app.run()