#!/usr/bin/env bash

set -eu

DEBIAN_FRONTEND=noninteractive apt-get install -y socat git git-svn debhelper dh-autoreconf \
    libarchive-dev libgtk-3-dev libticables-dev libticalcs-dev libticonv-dev libtifiles-dev