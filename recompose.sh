#!/bin/bash
docker-compose down
docker image rm fvweb-web
docker-compose up -d
