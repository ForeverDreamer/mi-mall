#!/usr/bin/env bash

set -x

set -eo pipefail

source ./deploy.sh

docker-compose build

docker-compose up