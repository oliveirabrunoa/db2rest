from flask import Blueprint, jsonify, request
from . import models
from backend import db
import datetime


course_type = Blueprint("course_type", __name__)

@course_type.route('/course_type', methods=['GET'])
def course_type_teste():
    c = models.CourseType.query.all()
    print(c)
    return jsonify({})
