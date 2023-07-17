#!/bin/bash

cd /root/mlh-portfolio-site

# Fetch the latest changes from the main branch and reset the local repository
git fetch && git reset origin/main --hard

# Activate the Python virtual environment and install dependensies
source python3-virtualenv/bin/activate
pip install -r requirements.txt

# Systemctl
systemctl daemon-reload
systemctl restart myportfolio.service

echo "Complete."