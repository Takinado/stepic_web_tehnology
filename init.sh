#!/usr/bin/env bash
sudo rm /etc/nginx/sites-enabled/default
sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
#python /home/box/web/tests.py

sudo ln -sf /home/box/web/etc/hello.py /etc/gunicorn.d/hello.py
sudo ln -sf /home/box/web/etc/django.py /etc/gunicorn.d/django.py

sudo /etc/init.d/gunicorn restart

#gunicorn -c /etc/gunicorn.d/hello.py hello:application

#cd /home/box/web/ask/
#gunicorn -c /etc/gunicorn.d/django.py ask.wsgi:application
#sudo gunicorn ask.wsgi:application




