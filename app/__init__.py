import os
import jinja2
import datetime
from flask import Flask, render_template, request, abort, jsonify
from dotenv import load_dotenv
# from peewee import MySQLDatabase
from peewee import *
from playhouse.shortcuts import model_to_dict

load_dotenv()
# create Flask server (__name__ means the current file)
app = Flask(__name__)

if os.getenv("TESTING") == "true":
    print("Running in test mode")
    mydb = SqliteDatabase('file:memory?mode=memory&cache=shared', uri=True)
else:
    mydb = MySQLDatabase(os.getenv("MYSQL_DATABASE"),
        user=os.getenv("MYSQL_USER"),
        password=os.getenv("MYSQL_PASSWORD"),
        host=os.getenv("MYSQL_HOST"),
        port=3306)

print(mydb)

class TimelinePost(Model):
    name = CharField()
    email = CharField()
    content = TextField()
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = mydb

mydb.connect()
mydb.create_tables([TimelinePost])
                     

# decorator registers function as a custom error handler

@app.errorhandler(404)
def page_not_found(error):
    render_template('404.html'), 404

# default page

@app.route('/')
def index():
    # render_template(): searches for specified template and renders it
    return render_template('index.html', title="MLH Fellows", url=os.getenv("URL"))

# Routes within Jiya's portfolio
@app.route('/jiya_base')
def jiya_base():
    return render_template('jiya/jiya_base.html', title="About Jiya", url=os.getenv("URL"))

@app.route('/jiya_work')
def jiya_work():
    return render_template('jiya/jiya_work.html', title="Jiya's Work", url=os.getenv("URL"))

@app.route('/jiya_hobbies')
def jiya_hobbies():
    return render_template('jiya/jiya_hobbies.html', title="Jiya's Hobbies", url=os.getenv("URL"))

# Routes within Chizy's portfolio
@app.route('/chizy_base')
def chizy_base():
    return render_template('chizy/chizy_base.html', title="About Chizy", url=os.getenv("URL"))

@app.route('/chizy_work')
def chizy_work():
    return render_template('chizy/chizy_work.html', title="Chizy's Work", url=os.getenv("URL"))

@app.route('/chizy_hobbies')
def chizy_hobbies():
    return render_template('chizy/chizy_hobbies.html', title="Chizy's Hobbies", url=os.getenv("URL"))

@app.route('/timeline')
def timeline():
    return render_template('timeline.html', title="Timeline")

@app.route('/api/timeline_post', methods=['POST'])
def post_timeline_post():
    name = request.json.get('name')
    email = request.json.get('email')
    content = request.json.get('content')

    # Validate the name
    if not name:
        return jsonify({"error": "Invalid name"}), 400
    
    # Validate the email
    if not email or '@' not in email:
        return jsonify({"error": "Invalid email"}), 400
    
    # Validate the content
    if not content:
        return jsonify({"error": "Invalid content"}), 400

    timeline_post = TimelinePost.create(name=name, email=email, content=content)
    return jsonify(model_to_dict(timeline_post))

@app.route('/api/timeline_post', methods=['GET'])
def get_time_line_post():
    return {
        'timeline_posts': [model_to_dict(p) for p in TimelinePost.select().order_by(TimelinePost.created_at.desc())]
    }

@app.route('/api/timeline_post/<id>', methods=['DELETE'])
def delete_time_line_post(id):
    try: 
        timeline_post = TimelinePost.get(TimelinePost.id == id)
        timeline_post.delete_instance()
        return '', 204
    except TimelinePost.DoesNotExist:
        abort(404)

# put app in debug mode
if __name__ == "__main__":
    app.run(debug=True)
