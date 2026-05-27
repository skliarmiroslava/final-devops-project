from flask import Flask, jsonify  #take Flask class from flask library

import socket  #Python module for networking(get name pods/container)

import os

app = Flask(__name__) #create main web application)

@app.route("/") #route=URL path

def home():
    hostname = socket.gethostname()
    version = os.getenv("VERSION", "unknown")
    return jsonify ({
        "status" : "running",
        "hostname": hostname,  #return hostname_container
        "version": version
    }), 200

@app.route("/health")

def health():
    return jsonify({
        "health": "ok"
    }),200
if __name__== "__main__":    # protection against accidental code execution during import
    app.run(host="0.0.0.0",port=5000)

