#!/bin/sh
gunicorn app:app -w 10 --threads 10 -b 0.0.0.0:30 --capture-output
