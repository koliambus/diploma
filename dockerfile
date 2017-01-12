FROM ubuntu:latest
MAINTAINER Mykola Melnychuk "koliambus@ukr.net"
RUN apt-get update -y
RUN apt-get install -y python3-pip
RUN mkdir app
COPY hello.py /app
COPY requirements.txt /app
WORKDIR /app
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
ENTRYPOINT ["python3"]
CMD ["hello.py"]
