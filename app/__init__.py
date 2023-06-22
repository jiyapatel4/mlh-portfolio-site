import os
# import Flask module
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
# create Flask server (__name__ means the current file)
app = Flask(__name__)


# default page
@app.route('/')
def index():
    # render_template(): searches for specified template and renders it
    return render_template('index.html', title="MLH Fellow", url=os.getenv("URL"))

# route to /jiya_portfolio
@app.route('/jiya_portfolio')
def jiya_portfolio():
    return render_template('jiya_portfolio.html')