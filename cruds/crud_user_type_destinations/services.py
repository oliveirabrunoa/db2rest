from flask import Blueprint, jsonify
from . import models
from cruds.crud_user_type_destinations_user_type.models import UserTypeDestinationsUserType
from cruds.crud_user_type.models import UserType
from cruds.crud_users.models import Users
from backend import db
from . import serializer


user_type_destinations = Blueprint("user_type_destinations", __name__)


@user_type_destinations.route('/destinations_by_user_type/<user_type>', methods=['GET'])
def destinations_by_user_type(user_type):
    destinations = (db.session.query(models.UserTypeDestinations).
                                 filter(models.UserTypeDestinations.id == UserTypeDestinationsUserType.user_type_destination_id).
                                 filter(UserTypeDestinationsUserType.user_type_id == UserType.id).
                                 filter(UserType.id == user_type).all())
    return jsonify(destinations_by_user_type=serializer.UserTypeDestinationsSerializer().serialize(destinations, user_type))
