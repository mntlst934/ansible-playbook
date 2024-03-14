#!/bin/bash

# Create the systemd service file
cat <<EOF > /etc/systemd/system/dummy-service.service
[Unit]
Description=Dummy Service

[Service]
Type=simple
ExecStart=/usr/bin/bash -c 'while true; do echo "Dummy service is running..." >> /var/log/dummy-service.log; sleep 10; done'
Restart=always

[Install]
WantedBy=multi-user.target
EOF