from backend import db
from . import models
from cruds.crud_courses.models import Courses
from cruds.crud_course_sections.models import CourseSections
from cruds.crud_users.models import Users
from sqlalchemy import or_, func
import importlib

class Manager:

    def teachers_course_sections(self, teacher_id):
        return [course_section for course_section in CourseSections.query.filter_by(teacher_id=teacher_id)]

    def course_sections_students(self, course_sections_list):
        course_section_students=[]
        for course_section in course_sections_list:
            course_section_students.extend(models.CourseSectionStudents.query.filter_by(course_section_id=course_section.id, status=1).all())
        return [Users.query.get(cs.user_id) for cs in course_section_students]
