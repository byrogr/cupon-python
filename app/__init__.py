from flask import Flask
from .config import Config

from .public import public


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.register_blueprint(public)
    return app