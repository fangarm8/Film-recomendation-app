from flask import Flask
from .ext import db
from .config import Config

def create_app(config_info = Config):
    app = Flask(__name__)
    app.config.from_object(config_info)

    db.init_app(app)

    from .routes import register_routes
    register_routes(app)

    return app