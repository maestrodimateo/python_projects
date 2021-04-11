from flask import Blueprint, request, Response
from api.schemas.userschema import UserSchema
from marshmallow import ValidationError
from api.utils import validate_fields
from api.models.user import User
from api import db

user = Blueprint('user', __name__, url_prefix='/api/users')

BAD_REQUEST = 400

user_schema = UserSchema()

@user.route('/signup', methods = ['POST'])
def signup():
    try:
        fields = validate_fields(user_schema, request)
    except ValidationError as err:
        return err.messages, BAD_REQUEST

    fields.pop('password_confirmation')
    new_user = User(**fields)
    last_added = new_user.create()
    return {'message': 'User added with success', 'user': user_schema.dump(last_added)}

@user.route('/login', methods = ['GET'])
def login():
    try:
        fields = validate_fields(user_schema, request, partial= ('password_confirmation', 'username'))
    except ValidationError as err:
        return err.messages, BAD_REQUEST
    