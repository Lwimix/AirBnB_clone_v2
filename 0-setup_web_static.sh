#!/usr/bin/env bash
#This script creates directories for deployment
sudo apt update && sudo apt -y install nginx
sudo mkdir -p /data && sudo mkdir -p /data/web_static
sudo mkdir -p /data/web_static/releases
sudo mkdir -p /data/web_static/shared
sudo mkdir -p /data/web_static/releases/test/
sudo echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html
sudo rm -f /data/web_static/current
sudo ln -s /data/web_static/releases/test/ /data/web_static/current
sudo chmod -R 755 /data/
sudo sed -i '53 i \\tlocation /hbnb_static {\\talias /data/web_static/current;\n\t}' /etc/nginx/sites-available/default
sudo systemctl reload nginx
