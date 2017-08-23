from flask import Blueprint, jsonify
from . import models
from cruds.crud_users.models import Users
from cruds.crud_course_sections.models import CourseSections
from cruds.crud_course_section_students.models import CourseSectionStudents
from backend import db
from . import serializer


student_attendance = Blueprint("student_attendance", __name__)


@student_attendance.route('/students_attendance/<course_section_id>/<student_id>', methods=["GET"])
def students_attendance(course_section_id, student_id):

    students_attendance_list = (db.session.query(models.StudentAttendance).
                                 filter(models.StudentAttendance.course_section_student_id == CourseSectionStudents.id).
                                 filter(CourseSectionStudents.course_section_id == course_section_id).
                                 filter(CourseSectionStudents.user_id == student_id).all())

    students_attendance = serializer.StudentAttendanceSerializer().serialize(students_attendance_list)
    return jsonify(students_attendance=students_attendance)
