from MapToRest.db_model import CourseTypeBase


class CourseType(CourseTypeBase):

    __modelname__ = 'CourseType'

    __tablename__ = 'course_type'

    __attributes__ = [{"name":"id", "type": "Integer", "primary_key": True},
                     {"name":"description", "type":"String", "max_lenght": 50}]

    def __init__(self, description):
        super().__init__(self, id, description)
