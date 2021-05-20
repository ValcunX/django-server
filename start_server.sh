#! /bin/sh

gunicorn --bind 127.0.0.1:8000 --daemon --workers 3 django_server.wsgi:application 
nginx -g "daemon off;"
