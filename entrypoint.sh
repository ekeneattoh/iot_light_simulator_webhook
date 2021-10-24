#!/bin/bash
exec gunicorn --config gunicorn_config.py light_simulator:application