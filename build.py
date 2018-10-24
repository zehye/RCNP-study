#!/usr/bin/env python

import os
import subprocess

try:
    subprocess.call('pipenv lock --requirements > requirements.txt', shell=True)
    subprocess.call('docker build -t eb-docker-study:base -f Dockerfile.base .', shell=True)
finally:
    os.remove('requirements.txt')
