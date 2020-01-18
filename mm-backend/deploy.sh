#!/usr/bin/env bash

set -x

set -eo pipefail

mkdir static_in_env

python src/manage.py collectstatic