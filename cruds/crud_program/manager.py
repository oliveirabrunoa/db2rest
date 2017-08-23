from backend import db
from . import models
from cruds.crud_courses.models import Courses
from cruds.crud_course_section_students.models import CourseSectionStudents
from cruds.crud_course_sections.models import CourseSections
from cruds.crud_users.models import Users
from sqlalchemy import or_, func


class Manager:

    def course_times_by_student(self, course, student):
        return (db.session.query(func.count(CourseSectionStudents.id)).
                                        filter(CourseSectionStudents.course_section_id == CourseSections.id).
                                        filter(CourseSections.course_id == Courses.id).
                                        filter(Courses.program_id == models.Program.id).
                                        filter(models.Program.id == student.program_id).
                                        filter(CourseSectionStudents.user_id == student.id).
                                        filter(Courses.id == course.id).
                                        filter(or_ (CourseSectionStudents.status == 2,
                                                    CourseSectionStudents.status == 3)).
                                        group_by(Courses.code,Courses.program_section).order_by(Courses.program_section).first())

    def hours_and_credits_completed(self, student):
        return (db.session.query(func.sum(Courses.hours), func.sum(Courses.credits)).
                                        filter(CourseSectionStudents.course_section_id == CourseSections.id).
                                        filter(CourseSections.course_id == Courses.id).
                                        filter(Courses.program_id == models.Program.id).
                                        filter(models.Program.id == student.program_id).
                                        filter(CourseSectionStudents.user_id == student.id).
                                        filter(CourseSectionStudents.status == 2).
                                        group_by(models.Program.id).first())

    def last_course_section_student(self, course, student):
        return (db.session.query(CourseSectionStudents).
                                        filter(CourseSectionStudents.course_section_id == CourseSections.id).
                                        filter(CourseSections.course_id == Courses.id).
                                        filter(Courses.program_id == models.Program.id).
                                        filter(models.Program.id == student.program_id).
                                        filter(CourseSectionStudents.user_id == student.id).
                                        filter(Courses.id == course.id).
                                        order_by(CourseSections.course_section_period.desc()).first())

    def programs_users(self, program_id, user_type):
        return (db.session.query(Users).
                                        filter(models.Program.id==Users.program_id).
                                        filter(models.Program.id==program_id).
                                        filter(Users.type==user_type).all())
