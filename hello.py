# -*- coding: utf-8 -*-
import optparse
import requests
from flask import Flask

app = Flask(__name__)

this_container_number = 0
default_port = 5000


@app.route("/")
def hello():
    return "Flask Dockerized, my container number = " + this_container_port


@app.route("/hello/<int:container>")
def hello_container(container):
    return "Hello from container #" + str(container) + " through container #" + str(this_container_port)


@app.route("/connect/<string:address>")
def connect(address):
    return requests.get("http://" + address + ":" + str(default_port) + "/hello/" + str(this_container_port)).content


def parse_container():
    parser = optparse.OptionParser()
    parser.add_option("-C", "--container", dest="container", default=0)
    options, _ = parser.parse_args()
    return options.container


if __name__ == "__main__":
    this_container_port = parse_container()
    app.run(host="0.0.0.0", port=default_port)
