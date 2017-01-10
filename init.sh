#!/usr/bin/env bash
sudo ln -sf /home/box/web/etc/hello.conf  /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
#python /home/box/web/tests.py

sudo ln -sf /home/box/web/etc/hello.py  /etc/gunicorn.d/hello.py
sudo /etc/init.d/gunicorn restart
#gunicorn -b 0.0.0.0:8080 hello:app