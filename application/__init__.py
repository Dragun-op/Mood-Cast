from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import Config

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    login_manager.init_app(app)

    from application.auth.routes import auth_bp
    from application.mood.routes import mood_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(mood_bp)

    return app