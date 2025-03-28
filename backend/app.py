from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    
    app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:dogsarecool@localhost:5432/falshCardsAPP_db"
    
    app.secret_key = 'TEMPSECRETKEY'
    
    db.init_app(app)
    
    # TODO: user login implementation
    
    # TODO: import models
    
    # TODO: create the bycrypt for hashing the users passwords
    # TODO: import routes
    
    migrate = Migrate(app, db)
    
    return app
