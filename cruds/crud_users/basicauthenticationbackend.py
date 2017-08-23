from . import models
from flask import jsonify
from cruds.crud_program.models import Program
from cruds.crud_user_type.models import UserType
from . import serializer


class BasicAuthenticationBackend:

    def authenticate(self, email, password):
        user = models.Users.query.filter_by(email=email, password=password).first()
        if user:
            user_serialized = serializer.UsersSerializer().serialize([user])
            return jsonify(user=user_serialized), 200
        else:
            return jsonify(result='Invalid email or password'), 404
