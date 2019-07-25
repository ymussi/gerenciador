#!/bin/bash

cd /app/gerenciador/gerenciador

gunicorn app:app --bind 0.0.0.0:5000 -w 4 --reload --access-logfile -

