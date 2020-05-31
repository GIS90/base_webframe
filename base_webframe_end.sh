#!/usr/bin/env bash


.venv/bin/gunicorn -c etc/dev/gunicorn.conf wsgi:app