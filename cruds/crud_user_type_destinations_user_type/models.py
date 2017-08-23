from backend import db
from cruds.crud_user_type.models import UserType
from cruds.crud_user_type_destinations.models import UserTypeDestinations


class UserTypeDestinationsUserType(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_type_id = db.Column(db.Integer, db.ForeignKey('user_type.id'), nullable=False)
    user_type_destination_id = db.Column(db.Integer, db.ForeignKey('user_type_destinations.id'), nullable=False)
    user_type = db.relationship("UserType")
    __table_args__ = (db.UniqueConstraint('user_type_id','user_type_destination_id', name='user_type_destinations_user_type_uc'),)

    def set_fields(self, fields):
        self.user_type_id = fields['user_type_id']
        self.user_type_destination_id = fields['user_type_destination_id']
