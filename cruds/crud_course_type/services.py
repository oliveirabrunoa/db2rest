from flask import Blueprint, jsonify, request
from . import models
from MapToRest import db_model as models
from backend import db, db_session
import datetime


course_type = Blueprint("course_type", __name__)

@course_type.route('/course_type', methods=['GET'])
def course_type_teste():
    course_types = models.CourseType.query.all()
    return jsonify(result=[dict(id=ct.id_course_type, description=ct.description_course_type) for ct in course_types])
