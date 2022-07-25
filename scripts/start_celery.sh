#!/bin/sh

sleep 35

celery -A apps.tasks.task worker -Q default --loglevel=debug
