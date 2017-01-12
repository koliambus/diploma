#!/usr/bin/env bash
docker stop -t 2 $(docker ps -q)