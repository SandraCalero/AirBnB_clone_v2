#!/usr/bin/env bash
# This script is setting up your web servers for the deployment of web_static
# Install nginx
sudo apt-get -y update
sudo apt-get -y install nginx

# Give ownership
sudo chown -R ubuntu:ubuntu /data/

# Create directories
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

# Create a fake HTML file
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html

# Create a symbolic link
ln -fs /data/web_static/releases/test/ /data/web_static/current

# Update the Nginx configuration to serve the content of /data/web_static/current/ to hbnb_static
file="/etc/nginx/sites-available/default"
sudo sed -i "/server_name _;/a location /hbnb_static/ {\\n\\talias /data/web_static/current/;}" $file

# Restart server
sudo service nginx restart
