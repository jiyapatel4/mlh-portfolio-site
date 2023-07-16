#!/bin/bash -x
# MLH PE work

# Kill all existing tmux sessions
tmux kill-server

cd /root/mlh-portfolio-site

# Fetch the latest changes from the main branch and reset the local repository
echo "Fetching latest changes from Git..."
git fetch && git reset origin/main --hard
echo "Git fetch and reset complete."

# Activate the Python virtual environment and install dependensies
echo "Activating virtual environment and installing dependencies..."
source python3-virtualenv/bin/activate
pip install -r requirements.txt
echo "Virtual environment setup complete."

# Start a new detached Tmux session in the project directory
echo "Starting Flask server in a new tmux session..."
tmux new-session -d -s myproject 'cd /root/mlh-portfolio-site && source python3-virtualenv/bin/activate && export FLASK_ENV=production && flask run --host=0.0.0.0'
echo "Tmux session started."


echo "Deployment complete."