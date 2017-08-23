from MapToRest.db_model import BaseClass


class CourseType(BaseClass):

    __modelname__ = 'CourseType'

    __attributes__ = [{"name":"id", "type": "Integer", "primary_key": True},
                     {"name":"description", "type":"String", "max_lenght": 50}]

    def __init__(self, description):
        BaseClass.__init__(self, id, description)
