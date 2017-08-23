from . import models
from cruds.crud_course_type.serializer import CourseTypeSerializer
from cruds.crud_course_type.models import CourseType


class CoursesSerializer:

    def serialize(self, courses):
        data = []
        for course in courses:
            course_type = CourseType.query.get(course.course_type_id)

            data.append({
                'id': course.id,
                'code': course.code,
                'name': course.name,
                'credits':course.credits,
                'hours':course.hours,
                'program_section':course.program_section,
                'course_type_id':CourseTypeSerializer().serialize([course_type]),
                'program_id':course.program_id
            })

        return data 
