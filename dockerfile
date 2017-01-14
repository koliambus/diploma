FROM ubuntu:latest
MAINTAINER Mykola Melnychuk "koliambus@ukr.net"
ENV container_number 1
RUN apt-get update -y
RUN apt-get install -y python3-pip
RUN mkdir app
COPY hello.py /app
COPY requirements.txt /app
COPY python_run.sh /app
WORKDIR /app
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
CMD python3 hello.py -C $container_number
