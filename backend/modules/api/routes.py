# TODO: split the app into models(blueprints)
import uuid
from flask import jsonify, request
from flask_restx import Namespace, Resource, fields
from ..app import db
from ..models import Card as CardModel

api_namespace = Namespace('api/cards', description='Operations related to flashcards')


# Define the model for the data we expect in the request body
card_model = api_namespace.model('Card', {
    'front': fields.String(required=True, description='The card front phase'),  # String field
    'back': fields.String(required=True, description='The card back phase'),  # String field
})

@api_namespace.route('/cards')
class CardsList(Resource):
    def get(self):
        """ Get all cards"""
        cards = CardModel.query.all()
        if cards:
            return jsonify([{'cardId': card.card_uid, 'front': card.front, 'back': card.back} for card in cards])
        return jsonify({'message': 'No cards in the basket yet!'})
    
    @api_namespace.doc(description='Create a new card', 
                       responses={201: 'Success'})
    @api_namespace.expect(card_model)
    def post(self):
        """ Create a new card """
        data = request.json
        print(f'data is {data}')
        new_card = CardModel(front=data['front'], back=data['back'])
        db.session.add(new_card)
        db.session.commit()
        return jsonify({'message': 'Card created successfully'})


@api_namespace.route('/<string:cardId>')
class CardOperations(Resource):
    @api_namespace.doc(description='Endpoint for getting a card by its id', 
                       responses={200: 'Success', 404: 'Not Found'})
    def get(self, cardId):
        # docstring for documentation
        """ Getting card by id """
        card = CardModel.query.get(uuid.UUID(cardId))
        if card:
            return jsonify(card.to_json())
        return jsonify({'message': 'Card does not exists'}), 404
    
    @api_namespace.doc(description='Endpoint for deleteing a card by id', 
                       responses={200: 'Successful Deletion', 400: 'Invalide Request', 404: 'Not Found'})
    def delete(self, cardId):
        """ Delete card by id """
        try:
            card = CardModel.query.get(uuid.UUID(cardId))
            if card:
                db.session.delete(card)
                db.session.commit()
                return {'message': 'Card Deleted Successfully'}, 200
            else:
                return {'message': 'The card does not exist'}, 404
        except ValueError:
            return {'message': 'Invalid Request'}, 400
        
    @api_namespace.doc(description="Endpoint for updating a card by id",
                       responses={200: 'Successful Update', 400: 'Invalide Request', 404: 'Not Found'})
    @api_namespace.expect(card_model)
    def put(self, cardId):
        """ Update card by Id """
        try:
            card = CardModel.query.get(uuid.UUID(cardId))
            if card:
                data = request.json
                card.front = data["front"]
                card.back = data["back"]
                db.session.commit()
                return {'message': 'Card has been updated successfully'},200
            else:
                return {'message': 'The card does not exist'}, 404
        
        except ValueError:
            return {'message': 'Invalid Request'}, 400
    