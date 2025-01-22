from flask import Flask
from .database import db
from .config import Config
from .routes import register_routes

def create_app(config_info = Config):
    app = Flask(__name__, static_folder='../../frontend/static', template_folder='../../frontend/templates')
    app.config.from_object(config_info)

    db.init_app(app)

    register_routes(app)

    return app