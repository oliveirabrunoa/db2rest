from flask import Blueprint
from . import models
from MapToRest import db_model as models


user_type = Blueprint("user_type", __name__)
