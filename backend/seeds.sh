#!/bin/sh

PYTHONPATH=$(pwd):${PYTHONPATH} python3 ./app/db/seeds.py
