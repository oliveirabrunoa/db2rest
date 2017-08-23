from backend import db
from cruds.crud_courses.models import Courses


class CourseSections(db.Model):
    __tablename__ = 'course_sections'

    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(20))
    name = db.Column(db.String(50))
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'))
    teacher_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    course_section_period = db.Column(db.String(6))
    section_times = db.relationship("SectionTimes", backref='course_section', lazy='dynamic')

    __table_args__ = (db.UniqueConstraint('course_id','teacher_id','course_section_period','code', name='course_section_period_uc'),)

    def __str__(self):
        return str('{0} - {1}').format(str(Courses.query.get(self.course_id).code), str(self.course_section_period))

    def set_fields(self, fields):
        self.code = fields['code']
        self.name = fields['name']
        self.course_id = fields['course_id']
        self.teacher_id = fields['teacher_id']
        self.course_section_period = fields['course_section_period']
