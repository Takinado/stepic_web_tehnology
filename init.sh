#!/usr/bin/env bash
sudo rm /etc/nginx/sites-enabled/default
sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
#python /home/box/web/tests.py

sudo rm /etc/gunicorn.d/hello.py
sudo rm /etc/gunicorn.d/django.py

sudo ln -sf /home/box/web/etc/hello.py /etc/gunicorn.d/hello.py
sudo ln -sf /home/box/web/etc/django.py /etc/gunicorn.d/django.py

sudo /etc/init.d/gunicorn restart

#gunicorn -c /etc/gunicorn.d/hello.py hello:application

cd /home/box/web/ask
#gunicorn -b 0.0.0.0:8000  ask.wsgi:application
#gunicorn -c /etc/gunicorn.d/django.py ask.wsgi:application &
#gunicorn -b 0.0.0.0:8000 ask.wsgi:application &
#sudo gunicorn ask.wsgi:application




