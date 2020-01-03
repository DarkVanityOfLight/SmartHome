sock_file = open("/etc/systemd/system/gunicorn.socket")
sock_content = """[Unit]
Description=gunicorn socket

[Socket]
ListenStream=/run/gunicorn.sock

[Install]
WantedBy=sockets.target"""
sock_file.write(sock_content)
sock_file.flush()
service_file = open("/etc/systemd/system/gunicorn.service")
service_content = """[Unit]
Description=gunicorn daemon
Requires=gunicorn.socket
After=network.target

[Service]
User=server
Group=www-data
WorkingDirectory=/home/server/SmartHome
ExecStart=/home/server//myprojectenv/bin/gunicorn \
          --access-logfile - \
          --workers 3 \
          --bind unix:/run/gunicorn.sock \
          myproject.wsgi:application

[Install]
WantedBy=multi-user.target"""
