#!/usr/bin/env bash

set -eu

cd tilem
patch -p1 --forward < ../patch || true
./configure
make -j
cd ..
