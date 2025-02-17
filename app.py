import os
from os.path import join, dirname
from dotenv import load_dotenv

from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient

client = MongoClient('mongodb+srv://muhammadazril12:azril1207@cluster0.sf6orbp.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')

db = client.fanproject

app = Flask(__name__)

@app.route('/')
def home():
   return render_template('index.html')

@app.route("/homework", methods=["POST"])
def homework_post():
    # sample_receive = request.form['sample_give']
    name_receive = request.form['name_give']
    comment_receive = request.form['comment_give']
    doc = {
        'name': name_receive,
        'comment': comment_receive,
    }
    db.fanmessages.insert_one(doc)
    return jsonify({'msg':'Comment Posted!'})

@app.route("/homework", methods=["GET"])
def homework_get():
    message_list = list(db.fanmessages.find({}, {'_id': False}))
    return jsonify({'messages': message_list})

if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)