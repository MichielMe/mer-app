from flask import Flask
from flask_login import LoginManager

login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.secret_key = 'michiel watchlist app'
    
    # Flask-Login configuration
    login_manager.init_app(app)
    login_manager.login_view = 'main.login'
    
    from .views import main
    app.register_blueprint(main)
        
    return app
