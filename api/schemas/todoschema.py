from api.models.todo import Todo
from marshmallow import fields, Schema, validate

class TodoSchema(Schema):
    
    load_only = ('id',)
    dump_only = ('public_id', 'created_at')

    id = fields.Integer()
    name = fields.Str(required = True, validate = validate.Length(min = 5, max = 100))
    deadline = fields.DateTime
    public_id = fields.Str
    created_at = fields.DateTime
    owner_id