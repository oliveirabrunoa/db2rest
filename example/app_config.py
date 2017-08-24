from flask import Flask
import os
import importlib
import string
from blueprints.post import post
from blueprints.category import category


def create_app():
    app = Flask("example")

    app.config.from_object(os.environ['APP_SETTINGS'])
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    return app

app = create_app()
app.register_blueprint(post)
app.register_blueprint(category)

if __name__ == '__main__':
    app.run()
