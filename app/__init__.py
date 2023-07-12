import os
# import Flask module
from flask import Flask, render_template, request, abort
from dotenv import load_dotenv
from peewee import *

import jinja2

load_dotenv()
# create Flask server (__name__ means the current file)
app = Flask(__name__)

# MySQLDatabase is a funtion from peewee that lets us connect to the database
mydb = MySQLDatabase(os.getenv("MY_DATABASE"),
              user=os.getenv("MYSQL_USER"),
              password=os.getenv("MYSQL_PASSWORD"),
              host=os.getenv("MYSQL_HOST"),
              port=3306              
        )

print(mydb)


# decorator registers function as a custom error handler
@app.errorhandler(404)
def page_not_found(error):
    render_template('404.html'), 404

# default page


@app.route('/')
def index():
    # render_template(): searches for specified template and renders it
    return render_template('index.html', title="MLH Fellows", url=os.getenv("URL"))

# routes within Jiya's portfolio


@app.route('/jiya_base')
def jiya_base():
    return render_template('jiya/jiya_base.html', title="About Jiya", url=os.getenv("URL"))


@app.route('/jiya_work')
def jiya_work():
    return render_template('jiya/jiya_work.html', title="Jiya's Work", url=os.getenv("URL"))


@app.route('/jiya_hobbies')
def jiya_hobbies():
    return render_template('jiya/jiya_hobbies.html', title="Jiya's Hobbies", url=os.getenv("URL"))


@app.route('/chizy_base')
def chizy_base():
    return render_template('chizy/chizy_base.html', title="About Chizy", url=os.getenv("URL"))


@app.route('/chizy_work')
def chizy_work():
    return render_template('chizy/chizy_work.html', title="Chizy's Work", url=os.getenv("URL"))


@app.route('/chizy_hobbies')
def chizy_hobbies():
    return render_template('chizy/chizy_hobbies.html', title="Chizy's Hobbies", url=os.getenv("URL"))


# put app in debug mode
if __name__ == "__main__":
    app.run(debug=True)
