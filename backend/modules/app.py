from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restx import Api, Resource
from flask_swagger_ui import get_swaggerui_blueprint

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    
    app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:dogsarecool@localhost:5432/falshCardsAPP_db"
    app.secret_key = 'TEMPSECRETKEY'
    
    db.init_app(app)
    
    # TODO: user login implementation
    
    # TODO: import models
    
    # TODO: create the bycrypt for hashing the users passwords
    
    api = Api(app, version='1.0', title='FlashCards API', description='A simple API for practicing', doc='/swagger')
    SWAGGER_URL = '/swagger'
    API_URL = ''
    
    swagger_ui_bluprint = get_swaggerui_blueprint(
        SWAGGER_URL,
        API_URL,
        config = {'app_name': 'Flask Swagger UI simple practice'}
    )
    # api.namespace('api', description='Sample operation')
    from .api.routes import api_namespace
    api.add_namespace(api_namespace, path='/api')
    
    from .models import Card
    migrate = Migrate(app, db)
    
    return app
