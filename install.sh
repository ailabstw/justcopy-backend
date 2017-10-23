#!/bin/bash

DEBIAN_FRONTEND=noninteractive apt-get install -y python-dev python3.5

apt-get install -y python3-pip
pip3 install http://download.pytorch.org/whl/cu80/torch-0.2.0.post3-cp35-cp35m-manylinux1_x86_64.whl
pip3 install -r requirements.txt

source setup.sh

mkdir -p $POSTS
