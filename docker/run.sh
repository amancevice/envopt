#!/bin/bash

docker-compose up -d > /dev/null 2>&1
docker-compose logs envopt_0
echo
docker-compose logs envopt_1
docker-compose down --rmi local > /dev/null 2>&1
