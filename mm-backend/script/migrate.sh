#!/usr/bin/env bash

set -x

set -eo pipefail

#if [[ $1 = '-m' ]]; then
#    docker-compose exec web python src/manage.py migrate
#    docker-compose exec web python src/manage.py loaddata mm_db.json --exclude=auth.permission --exclude=contenttypes
#fi

docker-compose exec web python src/manage.py migrate
docker-compose exec web python src/manage.py loaddata mm_db.json --exclude=auth.permission --exclude=contenttypes