from . import models
from cruds.crud_courses.serializer import CoursesSerializer
from cruds.crud_courses.models import Courses


class CourseSectionsSerializer:

    def serialize(self, course_sections):
        data = []
        for course_section in course_sections:
            course = Courses.query.get(course_section.course_id)

            data.append({
                'id': course_section.id,
                'code': course_section.code,
                'name': course_section.name,
                'course': CoursesSerializer().serialize([course]),
                'teacher_id':  course_section.teacher_id,
                'course_section_period': course_section.course_section_period
            })

        return data 
