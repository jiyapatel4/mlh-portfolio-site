#!/bin/bash
tmux kill-server
cd mlh-portfolio-site-deploy
git fetch && git reset origin/main --hard
python -m venv python3-virtualenv
source python3-virtualenv/bin/activate
pip install -r requirements.txt

tmux new-session -d -s "$test"
tmux send-keys -t "$test" 'python -m venv python3-virtualenv' Enter 'source python3-virtualenv/bin/activate' Enter 'flask run --host=jiya-patel.duckdns.org' Enter
