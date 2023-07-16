#!/bin/bash -x
# MLH PE work

# Kill all existing tmux sessions
tmux kill-server

cd /root/mlh-portfolio-site

# Fetch the latest changes from the main branch and reset the local repository
git fetch && git reset origin/main --hard

# Activate the Python virtual environment and install dependensies
source python3-virtualenv/bin/activate
pip install -r requirements.txt

# Start a new detached Tmux session in the project directory
tmux new-session -d -s myproject 'cd /root/mlh-portfolio-site && source python3-virtualenv/bin/activate && export FLASK_ENV=production && flask run --host=0.0.0.0'

echo "Deployment complete."
