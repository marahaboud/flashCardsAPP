import uuid
from sqlalchemy_utils import UUIDType
from .app import db

class Card(db.Model):
    __tablename__ = 'cards'
    
    card_uid = db.Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
    front = db.Column(db.String, nullable=False)
    back = db.Column(db.String, nullable=False)
    
    def to_json(self):
        return {
            "cardId": str(self.card_uid),
            "front": self.front,
            "back": self.back
        }