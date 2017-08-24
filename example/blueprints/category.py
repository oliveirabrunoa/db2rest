from flask import Blueprint, jsonify, request
import datetime

category = Blueprint("category", __name__)

@category.route('/category')
def hello():
    return "Hello World!"
