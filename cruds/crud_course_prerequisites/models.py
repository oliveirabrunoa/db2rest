from backend import db


class CoursePrerequisites(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    program_id = db.Column(db.Integer, db.ForeignKey('program.id'), nullable=False)
    course_id_from = db.Column(db.Integer, db.ForeignKey('courses.id'), nullable=False)
    course_id_to = db.Column(db.Integer, db.ForeignKey('courses.id'), nullable=False)

    def serialize(self):
        return {
            'id': self.id,
            'program_id': self.program_id,
            'course_id_from': self.course_id_from,
            'course_id_to': self.course_id_to
        }

    def set_fields(self, fields):
        self.program_id = fields['program_id']
        self.course_id_from = fields['course_id_from']
        self.course_id_to = fields['course_id_to']
