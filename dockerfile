FROM ubuntu:latest
MAINTAINER Mykola Melnychuk DA-52c "koliambus@ukr.net"
ENV container_number 1
RUN mkdir app
COPY . /app
WORKDIR /app
RUN apt-get update -y
RUN apt-get install -y python3-pip
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
EXPOSE 5000
CMD python3 hello.py -C $container_number
