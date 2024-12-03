#!/bin/sh

set -e

# flask wait_for_db

gunicorn --bind :5000 --workers 4 "main.py"
