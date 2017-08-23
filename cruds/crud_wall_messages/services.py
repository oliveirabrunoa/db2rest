from flask import jsonify, Blueprint, request
from . import models
from backend import db
from cruds.crud_user_type_destinations.models import UserTypeDestinations
from cruds.crud_user_type_destinations_user_type.models import UserTypeDestinationsUserType
from cruds.crud_user_type.models import UserType
from cruds.crud_wall_messages.models import WallMessages
from cruds import get_paginated_list, format_urls_in_text
import pytz
import datetime
import requests
import settings
import json
from pyfcm import FCMNotification
from sqlalchemy import desc
from sqlalchemy import or_
import calendar
from . import serializer
from cruds.crud_users.models import Users


wall_messages = Blueprint("wall_messages", __name__)
push_service = FCMNotification(api_key=settings.PUSH_NOTIFICATIONS_SETTINGS['API_NOTIFICATION_KEY'])


@wall_messages.route('/wall_messages/<param>', methods=['GET'])
def get_wall_messages(param):
    #param can be email or user id
    if param.isdigit():
        user = Users.query.get(param)
    else:
        user = Users.query.filter_by(email=param).first()

    if not user:
        return jsonify(result="Invalid user id")

    messages = []
    today_time_stamp = calendar.timegm(datetime.datetime.now(tz=pytz.timezone('America/Bahia')).timetuple())
    wall_messages_list = (db.session.query(models.WallMessages).
                                 filter(models.WallMessages.date >= today_time_stamp - (86400 * 14)).
                                 order_by(desc(models.WallMessages.date)).all())

    for message in wall_messages_list:
        users = set(message.get_destinations() + message.get_sender())

        if user in users:
            messages.append(message)

    messages_serialized = serializer.WallMessagesSerializer().serialize(messages)
    return jsonify(get_paginated_list(messages_serialized,
		                              '/wall_messages/' + str(user.id),
                                      start=int(request.args.get('start', 1)))), 200


@wall_messages.route('/wall_push_notification', methods=['POST'])
def wall_push_notification():
    _dict = {}

    post_message = request.get_json()['post_message']
    user_type_destination_id = post_message['user_type_destination_id']
    parameter = post_message['parameter']
    message = post_message['message']
    sender = post_message['sender']

    today_time_stamp = calendar.timegm(datetime.datetime.now(tz=pytz.timezone('America/Bahia')).timetuple())
    post_message['date'] = today_time_stamp
    wall_message = models.WallMessages()
    wall_message.set_fields(post_message)

    users = set(wall_message.get_destinations())
    result = send_message([user.push_notification_token for user in users],
                          message,
                          wall_message.get_sender()[0],
                          serializer.WallMessagesSerializer().serialize([wall_message])[0])
    print(result)
    db.session.add(wall_message)
    db.session.commit()

    message_serialized = serializer.WallMessagesSerializer().serialize(models.WallMessages.query.filter_by(sender=sender).all())
    return jsonify(wall_messages=message_serialized), 200


def send_message(users_tokens, body, sender, data_message=None):
    try:
        registration_ids = users_tokens
        message_title = 'Nova mensagem de {0}'.format(sender.name)
        message_body = body
        result = push_service.notify_multiple_devices(registration_ids=registration_ids, message_title=message_title,message_body=message_body, data_message=data_message)
        print(result)
        return True
    except:
        return False

@wall_messages.route('/search_wall_messages/<user_id>/<param>', methods=['GET'])
def search_wall_messages(user_id, param):
    user = models.Users.query.get(user_id)

    if not user:
        return jsonify(result="Invalid user id")

    messages = []
    today_time_stamp = calendar.timegm(datetime.datetime.now(tz=pytz.timezone('America/Bahia')).timetuple())
    wall_messages_list = (db.session.query(models.WallMessages).
                                 filter(models.WallMessages.date >= today_time_stamp - (86400 * 14)).
                                 filter(models.Users.id==models.WallMessages.sender).
                                 filter(or_(models.WallMessages.message.ilike('%{0}%'.format(param)),
                                            models.Users.name.ilike('%{0}%'.format(param)))).
                                 order_by(desc(models.WallMessages.id)).all())

    for message in wall_messages_list:
        users = set(message.get_destinations() + message.get_sender())

        if user in users:
            messages.append(message)
    messages_serialized = serializer.WallMessagesSerializer().serialize(messages)
    return jsonify(get_paginated_list(messages_serialized,
		                              '/search_wall_messages/{0}/{1}'.format(str(user.id),param),
                                      start=int(request.args.get('start', 1)))), 200
