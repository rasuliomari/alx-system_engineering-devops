# Web server Configs with HTTP header response.

# Install Nginx
exec { 'Installing nginx':
  command  => 'sudo apt-get -y update && sudo apt-get install -y nginx',
  provider => shell
}

# Add a custom HTTP header to the Nginx configuration
exec { 'HTTP header Response':
  command  => 'sudo sed -i "/server_name _/a add_header X-Served-By \$HOSTNAME;" /etc/nginx/sites-enabled/default',
  provider => shell
}

# Restart Nginx to apply the changes
exec { 'Restarting nginx':
  command  => 'sudo service nginx restart',
  provider => shell,
}
