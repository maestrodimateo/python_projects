from flask import request, jsonify
from api.models.user import User
from functools import wraps
from .utils import conf
import jwt

# check if the user is connected
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):

        token = None

        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']

        if not token:
            return jsonify({'message' : 'Token is missing!'}), 401

        data = jwt.decode(token, conf['secret_key'], algorithms="HS256")
        current_user = User.find_by_public_id(data['public_id'])

        if not current_user:
            return jsonify({'message' : "Token is invalid !"}), 401

        return f(*args, **kwargs)

    return decorated