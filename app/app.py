import socket  #Python module for networking(get name pods/container)

from flask import Flask, jsonify  #take Flask class from flask library

app = Flask(__name__) #create main web application)

@app.route("/") #route=URL path

def home():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return jsonify ({
        "status" : "running",
        "hostname": hostname,  #return hostname_container
        "ip_pod": ip_address,  #return ip pod
        "version": "1.0"
    }), 200

@app.route("/health")

def health():
    return jsonify({
        "health": "ok"
    }),200
if __name__== "__main__":    # protection against accidental code execution during import
    app.run(host="0.0.0.0",port=5000)

