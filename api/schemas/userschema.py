from api.models.user import User
from marshmallow import Schema, fields, validate, validates, validates_schema, ValidationError
from api.utils import password_crypt

class UserSchema(Schema):
    class Meta:
        load_only = ('password', 'password_confirmation', 'id')
        dump_only = ('public_id',)
    
    id = fields.Integer()
    username = fields.Str(required = True, validate = validate.Length(max = 100))
    email = fields.Email(required = True, validate = validate.Length(max = 150))
    public_id = fields.Str(required = True)
    picture = fields.Str()
    password = fields.Str(validate = validate.Length(min = 20), required = True)
    password_confirmation = fields.Str(required = True)

    @validates('username')
    def unique_username(self, value):
        user = User.query.filter_by(username = value).first()
        if user:
            raise ValidationError('Name already used')
    
    @validates('email')
    def unique_email(self, value):
        user = User.query.filter_by(email = value).first()
        if user:
            raise ValidationError('Email already used')
    
    @validates_schema
    def confirm_password(self, data, **kwarg):
        error = {}
        if not data['password_confirmation'] == data['password']:
            error['password_confirmation'] = "The password confirmation is not correct."
            raise ValidationError(error)
        
        data['password'] = password_crypt(data['password'])