from backend import db
from . import models


class UserTypeSerializer:

    def serialize(self, user_types):
        data=[]

        for user_type in user_types:
            data.append(
            {'id': user_type.id,
            'name': user_type.name,
            })

        return data
