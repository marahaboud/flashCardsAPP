# TODO: split the app into models(blueprints)
from flask import jsonify
from flask_restx import Namespace, Resource
from app import db
from models import Card

api_namespace = Namespace('api', description='Sample operation')

@api_namespace.route('/hi')
class Greet(Resource):
    def get(self):
        """ Greet Endpoing """
        return {'message': 'Hello from the other World!'}