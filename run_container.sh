#!/usr/bin/env bash
. stop_last.sh
#docker run -t -p 192.168.0.104:5000:5000 -d diploma:latest
docker run -t -p 5000:5000 -d diploma:latest