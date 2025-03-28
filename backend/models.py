from app import db

class Card(db.Model):
    __tablename__ = 'cards'
    
    card_uid = db.Column