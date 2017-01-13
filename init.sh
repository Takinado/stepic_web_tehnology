#!/usr/bin/env bash
sudo rm /etc/nginx/sites-enabled/default
sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart

sudo rm /etc/gunicorn.d/hello.py
sudo rm /etc/gunicorn.d/django.py

sudo ln -sf /home/box/web/etc/hello.py /etc/gunicorn.d/hello.py
sudo ln -sf /home/box/web/etc/django.py /etc/gunicorn.d/django.py

sudo /etc/init.d/gunicorn restart

