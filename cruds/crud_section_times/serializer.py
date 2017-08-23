from backend import db
from . import models
import datetime
from cruds.crud_course_sections.serializer import CourseSectionsSerializer


class SectionTimeSerializer:

    def serialize(self, section_times):
        data=[]

        for section_time in section_times:

            data.append(
            {'id': section_time.id,
            'week_day': section_time.week_day,
            'section_time_start_time': section_time.section_time_start_time.strftime("%H:%M:%S"),
            'section_time_finish_time':section_time.section_time_finish_time.strftime("%H:%M:%S"),
            'course_section': CourseSectionsSerializer().serialize([section_time.course_section])
            })

        return data
