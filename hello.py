# -*- coding: utf-8 -*-
import optparse
import requests
from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "Flask Dockerized, my container number = " + this_container


def parse_container():
    parser = optparse.OptionParser()
    parser.add_option("-C", "--container", dest="container", default=0)
    options, _ = parser.parse_args()
    return options.container


if __name__ == "__main__":
    this_container = parse_container()
    app.run(host='0.0.0.0')


@app.route("/hello/<int:container>")
def hello(container):
    return "Hello from container #" + container + " through container #" + this_container


@app.route("/connect/<int:port>")
def connect(port):
    return requests.get("192.168.0.104:" + port + "/hello/" + this_container)
