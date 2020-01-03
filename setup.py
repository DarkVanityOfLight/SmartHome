import os

sock_file = open("/etc/systemd/system/gunicorn.socket", "w+")
sock_content = """[Unit]
Description=gunicorn socket

[Socket]
ListenStream=/run/gunicorn.sock

[Install]
WantedBy=sockets.target"""
sock_file.write(sock_content)
sock_file.close()
service_file = open("/etc/systemd/system/gunicorn.service", "w+")
service_content = """[Unit]
Description=gunicorn daemon
Requires=gunicorn.socket
After=network.target

[Service]
User=server
Group=users
WorkingDirectory=/home/server/SmartHome
ExecStart=/home/server/.local/share/virtualenvs/SmartHome-EXIvxEz7/bin/gunicorn \
          --access-logfile - \
          --workers 3 \
          --bind unix:/run/gunicorn.sock \
          SmartHome.wsgi:application

[Install]
WantedBy=multi-user.target"""
service_file.write(service_content)
service_file.close()

os.system("sudo systemctl start gunicorn.socket && sudo systemctl enable gunicorn.socket")

nginx_site = open("/etc/nginx/sites-available/SmartHome", "w+")
nginx_content = """server {
    listen 80;
    server_name _;

    location = /favicon.ico { access_log off; log_not_found off; }
    location /static/ {
        root /home/server/SmartHome;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/run/gunicorn.sock;
    }
}"""
nginx_site.write(nginx_content)
nginx_site.close()

os.system("sudo ln -s /etc/nginx/sites-available/SmartHome /etc/nginx/sites-enabled && sudo systemctl restart nginx")
os.system("sudo ufw delete allow 8000 && sudo ufw allow 'Nginx Full'")
