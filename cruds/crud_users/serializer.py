from backend import db
from . import models
from cruds.crud_courses.models import Courses
from cruds.crud_course_section_students.models import CourseSectionStudents
from cruds.crud_course_sections.models import CourseSections
from cruds.crud_users.models import Users
from cruds.crud_user_type.models import UserType
from cruds.crud_program.models import Program
import datetime


class UsersSerializer:

    def serialize(self, users):
        data=[]
        for user in users:
            program = Program.query.get(user.program_id)
            user_type = UserType.query.get(user.type)

            data.append(
            {'id': user.id,
            'username': user.username,
            'email': user.email,
            'name': user.name,
            'birth_date': datetime.date.strftime(user.birth_date, "%m-%d-%Y") if user.birth_date  else user.birth_date,
            'gender': user.gender,
            'address': user.address,
            'push_notification_token': user.push_notification_token,
            'program_id': dict(id=program.id, abbreviation=program.abbreviation, name=program.name),
            'type': dict(id=user_type.id, name=user_type.name),
            'image_path': user.image_path,
            'course_sections': [dict(id=course_section_students.course_section.id, code=course_section_students.course_section.code) for course_section_students in user.course_sections if course_section_students.status==1]
            })

        return data if len(data) > 1 else data[0]
