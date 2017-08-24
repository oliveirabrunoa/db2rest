from flask import Blueprint, jsonify, request
import datetime

post = Blueprint("post", __name__)

@post.route('/post')
def hello():
    return "Hello World!"
