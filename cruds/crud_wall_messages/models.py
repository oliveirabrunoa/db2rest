import datetime
from backend import db
from cruds.crud_user_type_destinations.models import UserTypeDestinations
from cruds.crud_users.models import Users
from cruds import format_urls_in_text


class WallMessages(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date = db.Column(db.Integer)
    sender = db.Column(db.Integer, db.ForeignKey("users.id"))
    destination = db.Column(db.Integer, db.ForeignKey("user_type_destinations.id"))
    param_value = db.Column(db.Integer())
    message = db.Column(db.Text())

    def set_fields(self, fields):
        self.date = fields['date']
        self.sender = fields['sender']
        self.destination = fields['user_type_destination_id']
        self.param_value = fields['parameter']
        self.message = format_urls_in_text(fields['message'])

    def get_sender(self):
        return Users.query.filter_by(id=self.sender).all()

    def get_destinations(self):
        _dict = {}
        query = UserTypeDestinations.query.filter_by(id=self.destination).first().users_query
        query = str(query).replace('$', str(self.param_value))
        exec(query, _dict)
        return _dict['users']
