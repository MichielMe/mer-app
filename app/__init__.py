from flask import Flask
from .views import main
from .pyscripts.supa_handler import create_supa, read_supa, update_supa, delete_supa, supabase

def create_app():
    app = Flask(__name__)
    app.secret_key = 'michiel watchlist app'
    from .views import main
    app.register_blueprint(main)
        
    return app