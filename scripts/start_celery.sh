#!/bin/sh

sleep 35

MODE=$1 watchmedo auto-restart --directory=./  -p "*.py" --recursive -- celery -A apps.tasks.task worker -Q default --loglevel=debug &

