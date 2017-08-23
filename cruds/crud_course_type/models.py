from backend import BaseClass


class CourseType(BaseClass):
    """Course_type"""

    __tablename__ = 'course_type'

    def __str__(self):
        return self.name

    __unicode__ = __str__


    # id = db.Column(db.Integer, primary_key=True)
    # description = db.Column(db.String(50))
    #
    # def set_fields(self, fields):
    #     self.description = fields['description']
