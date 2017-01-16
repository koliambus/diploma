#!/usr/bin/env bash
. stop_last.sh
#docker run -t -e "container_number=2" --net flasknet --ip 172.18.0.2 -p 5002:5000 -d diploma:latest
docker run -t -p 5000:5000 -d diploma:latest