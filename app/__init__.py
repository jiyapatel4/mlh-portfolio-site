import os
# import Flask module
from flask import Flask, render_template, request, abort
from dotenv import load_dotenv


import jinja2

load_dotenv()
# create Flask server (__name__ means the current file)
app = Flask(__name__)

# decorator registers function as a custom error handler
@app.errorhandler(404)
def page_not_found(error):
    render_template('404.html'), 404

# default page
@app.route('/')
def index():
    # render_template(): searches for specified template and renders it
    return render_template('index.html', title="MLH Fellow", url=os.getenv("URL"))

# routes within Jiya's portfolio
@app.route('/jiya_base')
def jiya_base():
    return render_template('jiya_base.html', title="About Jiya", url=os.getenv("URL"))

@app.route('/jiya_work')
def jiya_work():
    return render_template('jiya_work.html', title="Jiya's Work", url=os.getenv("URL"))

@app.route('/jiya_hobbies')
def jiya_hobbies():
    return render_template('jiya_hobbies.html', title="Jiya's Hobbies", url=os.getenv("URL"))

# put app in debug mode
if __name__ == "__main__":
    app.run(debug=True)
