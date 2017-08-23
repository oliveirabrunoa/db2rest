from . import models
from cruds.crud_course_section_students_status.models import CourseSectionStudentsStatus
from cruds.crud_course_section_students_status.serializer import CourseSectionStudentsStatusSerializer


class CourseSectionStudentsSerializer:

    def serialize(self, course_section_students):
        data=[]
        for course_section_student in course_section_students:
            status = CourseSectionStudentsStatus.query.get(course_section_student.status)

            data.append({
                'id': course_section_student.id,
                'course_section_id': course_section_student.course_section_id,
                'user_id': course_section_student.user_id,
                'status': CourseSectionStudentsStatusSerializer().serialize([status]),
                'grade': course_section_student.grade
            })

        return data
