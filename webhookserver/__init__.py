from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from webhookserver.Config import Config


db = SQLAlchemy()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)

    from webhookserver.armbot_routes import main
    app.register_blueprint(main)

    return app
