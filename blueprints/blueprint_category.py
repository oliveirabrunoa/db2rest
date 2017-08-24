from flask import Blueprint, jsonify, request
import datetime
from Map2Rest import models

category = Blueprint("category", __name__)

@category.route('/categories')
def all_categories():
    categories = models.Category.query.all()
    return jsonify(result=[dict(id=ct.id_user_type, description=ct.name_user_type) for ct in categories])
