#!/bin/sh

sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
sudo rm -rf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
sudo mkdir /etc/gunicorn.d
sudo ln -sf /home/box/web/etc/gunicorn.conf.py /etc/gunicorn.d/hello
cd /home/box/web/etc
sudo gunicorn -chello hello:app &
