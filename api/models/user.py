from api import db
from uuid import uuid4

class User(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(100), nullable = False, unique = True)
    email = db.Column(db.String(150), nullable = False, unique = True)
    password = db.Column(db.String(255), nullable = False)
    public_id = db.Column(db.String(60), nullable = False, unique = True)
    picture = db.Column(db.String(60))

    @classmethod
    def find_by_username(cls, username: str) -> "User":
        return cls.query.filter_by(username = username).first()
    
    @classmethod
    def find_by_public_id(cls, public_id: str) -> "User":
        return cls.query.filter_by(public_id = public_id).first()
    
    @classmethod
    def find_by_email(cls, email: str) -> "User":
        return cls.query.filter_by(email = email).first()
    
    @classmethod
    def create(cls, fields: list) -> "User":
        new_user = cls(**fields, public_id = uuid4().hex)
        db.session.add(new_user)
        db.session.commit()
        return new_user