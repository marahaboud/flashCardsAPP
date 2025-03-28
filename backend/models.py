from app import db

class Card(db.Model):
    __tablename__ = 'cards'
    
    card_uid = db.Column(db.Integer, primary_key=True)
    front = db.Column(db.String, nullable=False)
    back = db.Column(db.String, nullable=False)
    
    def to_json(self):
        return {
            "cardId": self.card_uid,
            "front": self.front,
            "back": self.back
        }