from flask import Flask
from flask_login import LoginManager
import os
from flask_sqlalchemy import SQLAlchemy

login_manager = LoginManager()

db = SQLAlchemy()
DB_NAME = "database.db"
basedir = os.path.abspath(os.path.dirname(__file__))
DATABASE_URL = os.environ.get("DATABASE_URL") or f"sqlite:///{basedir}/{DB_NAME}"

def create_app():
    app = Flask(__name__)
    app.secret_key = 'michiel watchlist app'
    app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL
    db.init_app(app)
    
    # Flask-Login configuration
    login_manager.init_app(app)
    login_manager.login_view = 'main.login'
    
    from .views import main
    app.register_blueprint(main)
    
    with app.app_context():
        db.create_all()
        
    return app
