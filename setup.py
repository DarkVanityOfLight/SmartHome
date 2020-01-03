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
Group=root
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

