from api import db
from datetime import datetime
from uuid import uuid4

class Todo(db.Model):

    __tablename__ = 'todos'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable = False, unique = False)
    created_at = db.Column(db.DateTime, default = datetime.utcnow)
    deadline = db.Column(db.DateTime)
    public_id = db.Column(db.String(40), default = uuid4())
    owner_id = db.Column(db.Integer, db.ForeignKey('users.id'))