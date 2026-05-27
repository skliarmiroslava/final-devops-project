import socket  #Python module for networking(get name pods/container)

from flask import Flask, jsonify  #takr Flask class from flask library

app = Flask(__name__) #create main web application)

@app.route("/") #route=URL path

def home():
    return jsonify ({
        "status" : "running"
    }), 200

app.run(host="0.0.0.0",port=5000)

