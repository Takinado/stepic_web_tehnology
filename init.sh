#!/usr/bin/env bash
sudo ln -sf /home/takinado/projects/web/ /home/box/
sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx reload
