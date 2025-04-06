from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restx import Api, Resource
from flask_swagger_ui import get_swaggerui_blueprint
from flask_cors import CORS

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    CORS(app)
    
    app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:dogsarecool@localhost:5432/falshCardsAPP_db"
    app.secret_key = 'TEMPSECRETKEY'
    
    db.init_app(app)
    
    # TODO: user login implementation
    
    # TODO: import models
    
    # TODO: create the bycrypt for hashing the users passwords
    
    api = Api(app, version='1.0', title='FlashCards API', description='A simple API for practicing', doc='/swagger')
    SWAGGER_URL = '/swagger'
    API_URL = '/swagger.json'
    
    swagger_ui_bluprint = get_swaggerui_blueprint(
        SWAGGER_URL,
        API_URL,
        config = {'app_name': 'Flask Swagger UI simple practice'}
    )
    
    app.register_blueprint(swagger_ui_bluprint, url_prefix=SWAGGER_URL)
    
    # Serve the swagger json
    @app.route('/swagger.json')
    def serve_swagger():
        return api.__schema__
    
    # api.namespace('api', description='Sample operation')
    from .api.routes import api_namespace
    api.add_namespace(api_namespace, path='/api')
    
    from .models import Card
    migrate = Migrate(app, db)
    
    return app
