#!/usr/bin/env bash

set -x

set -eo pipefail

apt-get update

apt-get install -y libevent-dev

curl -SL -o $BUILD_ROOT/memcached.tar.gz https://memcached.org/files/memcached-1.5.20.tar.gz

mkdir $BUILD_ROOT/memcached

tar -xC $BUILD_ROOT/memcached --strip-components=1 -f $BUILD_ROOT/memcached.tar.gz

cd $BUILD_ROOT/memcached

./configure && make && make test && make install