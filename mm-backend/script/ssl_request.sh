#!/usr/bin/env bash

set -x

set -eo pipefail

docker run -it --rm --name certbot \
            -v "/etc/letsencrypt:/etc/letsencrypt" \
            -v "/var/lib/letsencrypt:/var/lib/letsencrypt" \
            -p 80:80 \
            certbot/certbot certonly --standalone -d itman.icu -d www.itman.icu

sudo cp -R /etc/letsencrypt/ ${HOME}/mm-backend

sudo chown -R $USER:$USER ${HOME}/mm-backend/letsencrypt