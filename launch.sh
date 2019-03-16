#!/bin/bash

set -eu

# sudo su -s /bin/bash nobody << EOF
socat TCP-LISTEN:2014,fork EXEC:"timeout 300 ./run.py"
# EOF
