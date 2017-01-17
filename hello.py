# -*- coding: utf-8 -*-
import optparse
import requests
from flask import Flask


class Parser:
    @staticmethod
    def parse_container():
        parser = optparse.OptionParser()
        parser.add_option("-C", "--container", dest="container", default=0)
        options, _ = parser.parse_args()
        return options.container


class Runner:
    @staticmethod
    def run(name, application):
        if name == "__main__":
            Config.container_number = Parser.parse_container()
            application.run(host="0.0.0.0", port=Config.default_port)


class Config:
    container_number = 0
    default_port = 5000
    app = None


class RoutesConfigurator:
    @staticmethod
    def configure(application):
        @application.route("/")
        def hello():
            return "Flask Dockerized, my container number = " + str(Config.container_number)

        @application.route("/hello/<int:container>")
        def hello_container(container):
            return "Hello from container #" + str(container) + " through container #" + str(Config.container_number)

        @application.route("/connect/<string:address>")
        def connect(address):
            connector = HttpConnector()
            return connector.connect("http://" + address + "/hello/" + str(Config.container_number)).content


class HttpConnector:
    def connect(self, address):
        return requests.get(address)

Config.app = Flask(__name__)

RoutesConfigurator.configure(Config.app)

Runner.run(__name__, Config.app)
