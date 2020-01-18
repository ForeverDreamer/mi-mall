#!/usr/bin/env bash

set -x

set -eo pipefail

if [[ ! -d static_in_env ]]; then
    mkdir static_in_env
fi

if [[ ! -d log ]]; then
    mkdir log && touch log/django.log log/mm.log && chmod -R 777 log
fi