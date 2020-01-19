#!/usr/bin/env bash

set -x

set -eo pipefail

PROJ_DIR=git_repos/mi-mall

cd ${HOME}/${PROJ_DIR}

git pull

if [[ -d ${HOME}/mm-backend ]]; then
    rm -rf ${HOME}/mm-backend
fi

cp -R mm-backend ${HOME}

cd ${HOME}/mm-backend/docker

if [[ $1 = 'http' ]]; then
    mv docker-compose.yml docker-compose-https.yml
    mv docker-compose-http.yml docker-compose.yml
fi

cd ../src/mm

mv settings.py settings_debug.py
mv settings_prod settings.py

cd ${HOME}/mm-backend/script

chmod u+x *.sh

source ./start.sh
