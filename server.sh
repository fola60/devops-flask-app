#!/bin/bash

python3 -m venv .my_venv

source .my_venv/bin/activate

pip3 install flask

flask --app hello run --host=0.0.0.0 --port=8080
