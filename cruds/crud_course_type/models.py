

class CourseType:

    __modelname__ = 'CourseType'

    __tablename__ = 'course_type'

    __attributes__ = [{"name":"id", "type": "Integer", "primary_key": True},
                     {"name":"description", "type":"String", "max_lenght": 50}]
