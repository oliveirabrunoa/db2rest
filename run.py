from flask import Flask
import os
import importlib
import string
from blueprints.blueprint_postagem import postagem
from blueprints.blueprint_categoria import categoria
from blueprints.blueprint_relationships import relationships


def create_app():
    app = Flask("example")

    app.config.from_object(os.environ['APP_SETTINGS'])
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    return app

app = create_app()
app.register_blueprint(postagem)
app.register_blueprint(categoria)
app.register_blueprint(relationships)

if __name__ == '__main__':
    app.run()
