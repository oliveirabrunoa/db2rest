from flask import Blueprint, jsonify, request
from . import models
from backend import db, db_session
import datetime


course_type = Blueprint("course_type", __name__)

@course_type.route('/course_type', methods=['GET'])
def course_type_teste():
    c = models.CourseType.query.first()
    d = models.CourseType("novo")
    print(d.teste())

    return jsonify({})
