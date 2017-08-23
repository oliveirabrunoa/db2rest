

class CourseType:

    __modelname__ = 'CourseType'

    __tablename__ = 'course_type'

    __attributes__ = [{"name":"id_course_type", "type": "Integer", "primary_key": True},
                     {"name":"description_course_type", "type":"String", "max_lenght": 50}]
