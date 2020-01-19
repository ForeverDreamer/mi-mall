#!/usr/bin/env bash

set -x

set -eo pipefail

docker run -it --rm --name certbot \
            -v "/etc/letsencrypt:/etc/letsencrypt" \
            -v "/var/lib/letsencrypt:/var/lib/letsencrypt" \
            -p 80:80 \
            certbot/certbot certonly --standalone -d crawleruniverse.com -d www.crawleruniverse.com

sudo cp -R /etc/letsencrypt/ .

sudo chown -R ec2-user:ec2-user letsencrypt