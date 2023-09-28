from flask import Flask
from .views import main


def create_app():
    app = Flask(__name__)
    app.secret_key = 'michiel watchlist app'
    from .views import main
    app.register_blueprint(main)
        
    return app