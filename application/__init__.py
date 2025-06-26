from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import Config
from flask_mail import Mail

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'
mail = Mail()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    from application.auth.routes import auth_bp
    from application.mood.routes import mood_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(mood_bp)

    from flask import render_template
    from datetime import datetime

    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('errors/404.html'), 404

    @app.errorhandler(500)
    def internal_error(e):
        return render_template('errors/500.html'), 500

    @app.context_processor
    def inject_current_year():
        return {'current_year': datetime.now().year}

    return app