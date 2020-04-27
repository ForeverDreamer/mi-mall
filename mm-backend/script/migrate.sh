#!/usr/bin/env bash

set -x

set -eo pipefail

#if [[ $1 = '-m' ]]; then
#    docker-compose exec web python src/manage.py migrate
#    docker-compose exec web python src/manage.py loaddata mm_db.json --exclude=auth.permission --exclude=contenttypes
#fi

cd ../docker

docker-compose exec web_backend python src/manage.py makemigrations
docker-compose exec web_backend python src/manage.py migrate
docker-compose exec web_backend python src/manage.py loaddata src/mm_db.json --exclude=auth.permission --exclude=contenttypes --exclude=admin.logentry --exclude=sessions.session