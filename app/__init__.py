from flask import Flask
from flask_login import LoginManager
import os
from flask_sqlalchemy import SQLAlchemy

login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.secret_key = 'michiel watchlist app'
    
    # Flask-Login configuration
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login' # type: ignore
    
    from .routes import main
    from .auth import auth_blueprint
    app.register_blueprint(main)
    app.register_blueprint(auth_blueprint, url_prefix='/auth')
        
    return app
