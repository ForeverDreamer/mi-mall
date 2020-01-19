#!/usr/bin/env bash

set -x

set -eo pipefail

ROOT_DIR=..

source ./deploy.sh

cd ${ROOT_DIR}/docker

docker build -f mod_wsgi.dockerfile -t doerlee/mod_wsgi ..

docker-compose build

docker-compose up