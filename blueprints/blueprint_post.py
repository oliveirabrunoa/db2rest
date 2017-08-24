from flask import Blueprint, jsonify, request
import datetime
from Map2Rest import models

post = Blueprint("post", __name__)

@post.route('/posts')
def all_posts():
    posts = models.Post.query.all()
    return jsonify(result=[dict(id=ct.id_course_type, description=ct.description_course_type) for ct in posts])
