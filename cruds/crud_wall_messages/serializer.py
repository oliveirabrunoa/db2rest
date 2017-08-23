from backend import db
from . import models
from cruds.crud_users.models import Users
from cruds.crud_user_type_destinations.models import UserTypeDestinations
import datetime
from cruds.crud_users.serializer import UsersSerializer
from cruds.crud_user_type_destinations.serializer import UserTypeDestinationsSerializer

class WallMessagesSerializer:

    def serialize(self, messages):
        data=[]

        for message in messages:
            sender = UsersSerializer().serialize([Users.query.get(message.sender)])
            user_type_destination = UserTypeDestinationsSerializer().serialize([UserTypeDestinations.query.get(message.destination)], message.param_value)
            data.append(
            {'id': message.id,
            'date': message.date,
            'sender': dict(id=sender['id'], name=sender['name'],email=sender['email'],program_id=sender['program_id'], type=sender['type']),
            'user_type_destination': user_type_destination[0],
            'message': message.message
            })

        return data
