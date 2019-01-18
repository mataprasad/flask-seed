#!/bin/bash

# Run application
uwsgi --http 0.0.0.0:5000 --module app.run:flaskApp --processes 1 --threads 8