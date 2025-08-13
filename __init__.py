
from flask import Flask
from .extensions import db
from app.routes import events_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    
    db.init_app(app)
   

    app.register_blueprint(events_bp)
    
    with app.app_context():
        db.create_all() 
    
    return app


