from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from .config import Config  # Import the Config class

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'routes.login'

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)  # Load config from Config class
    
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    
    from app import routes
    app.register_blueprint(routes.bp)
    
    return app
