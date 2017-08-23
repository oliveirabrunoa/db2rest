from backend import BaseClass


class CourseType(BaseClass):

    __tablename__ = 'course_type'

    __attribute__ = [{"id":"Integer", "primary_key":"True"},
                     {"description":"String(50)"}]

    def __init__(self, description):
        BaseClass.__init__(self, id, description)

    def __str__(self):
         return "{0}".format(self.__tablename__)
