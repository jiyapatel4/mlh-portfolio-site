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

# routes within Jiya's portfolio

@app.route('/jiya_about')
def jiya_about():
    return render_template('jiya_about.html')

@app.route('/jiya_work')
def jiya_work():
    return render_template('jiya_work.html')

@app.route('/jiya_hobbies')
def jiya_hobbies():
    return render_template('jiya_hobbies.html')

# put app in debug mode
if __name__ == "__main__":
    app.run(debug=True)