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

if [[ ! -d '/etc/letsencrypt/' ]]; then
    . ${HOME}/ssl_request.sh
else
    sudo cp -R /etc/letsencrypt/ ${HOME}/mm-backend
    sudo chown -R $USER:$USER ${HOME}/mm-backend/letsencrypt
fi

cp secret/* ${HOME}/mm-backend/src/mm/

cd ${HOME}/mm-backend/docker

if [[ $1 = 'http' ]]; then
    mv docker-compose.yml docker-compose-https.yml
    mv docker-compose-http.yml docker-compose.yml
fi

cd ../src/mm

mv settings.py settings_debug.py
mv settings_prod.py settings.py

cd ${HOME}/mm-backend/script

chmod u+x *.sh

source ./start.sh
