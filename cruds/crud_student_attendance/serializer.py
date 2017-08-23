from backend import db
import datetime


class StudentAttendanceSerializer:

    def serialize(self, student_attendances):
        data=[]

        for student_attendance in student_attendances:
            data.append(
            {'id': student_attendance.id,
            'section_time_id': student_attendance.section_time_id,
            'course_section_student_id': student_attendance.course_section_student_id,
            'status': student_attendance.status,
            'section_time_date':  datetime.date.strftime(student_attendance.section_time_date, "%m-%d-%Y")
            })

        return data
