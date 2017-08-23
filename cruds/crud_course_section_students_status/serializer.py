from . import models


class CourseSectionStudentsStatusSerializer:

    def serialize(self, course_section_students_status):
        data = []
        for status in course_section_students_status:
            data.append({
                'id': status.id,
                'description': status.description
            })

        return data 
