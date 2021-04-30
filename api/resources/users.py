from flask import Blueprint, request, Response
from api.schemas.userschema import UserSchema, UserLoginSchema
from marshmallow import ValidationError
from api.utils import validate_fields, jwt_encode
from api.models.user import User
from api import db

user = Blueprint('user', __name__, url_prefix='/api/users')

BAD_REQUEST = 400

user_schema = UserSchema()
user_login_schema = UserLoginSchema()

@user.route('/signup', methods = ['POST'])
def signup():
    try:
        fields = validate_fields(user_schema, request)
    except ValidationError as err:
        return err.messages, BAD_REQUEST

    fields.pop('password_confirmation')
    new_user = User.create(fields)
    return {'message': 'User added with success', 'user': user_schema.dump(new_user)}

@user.route('/login', methods = ['POST'])
def login():
    try:
        fields = validate_fields(user_login_schema, request, partial = ('password_confirmation', 'username'))
    except ValidationError as err:
        return err.messages, BAD_REQUEST
    
    user = User.find_by_email(fields['email'])
    token = jwt_encode(user.public_id)

    return {'message': 'Welcome {}'.format(user.username), 'user': user_login_schema.dump(user), 'token': token}
