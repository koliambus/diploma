# -*- coding: utf-8 -*-
import optparse
import requests
from flask import Flask

app = Flask(__name__)

this_container = 0


@app.route("/")
def hello():
    return "Flask Dockerized, my container number = " + this_container


@app.route("/hello/<int:container>")
def hello_container(container):
    return "Hello from container #" + str(container) + " through container #" + str(this_container)


@app.route("/connect/<int:port>")
def connect(port):
    return requests.get("http://127.0.0.1:" + str(port) + "/hello/" + str(this_container)).content


def parse_container():
    parser = optparse.OptionParser()
    parser.add_option("-C", "--container", dest="container", default=0)
    options, _ = parser.parse_args()
    return options.container


if __name__ == "__main__":
    this_container = parse_container()
    app.run(host='0.0.0.0')
