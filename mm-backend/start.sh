#!/usr/bin/env bash

set -x

set -eo pipefail

docker-compose build

docker-compose up