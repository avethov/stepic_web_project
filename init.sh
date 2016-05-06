#!/bin/sh

sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
sudo rm -rf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
cd /home/box/web/etc
sudo gunicorn -b 0.0.0.0:8080 hello:app &
