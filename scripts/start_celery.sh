#!/bin/sh

sleep 35

MODE=$1 watchmedo auto-restart --directory=./  -p "*.py" --recursive -- celery -A applications.v2.tasks.task worker -Q default --loglevel=debug &

