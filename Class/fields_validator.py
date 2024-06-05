from marshmallow import Schema, fields
from marshmallow.validate import Length
from Helpers.basic_helper import (
    validate_password as vp,
    validate_no_spaces as vns
)

class UserValidator(Schema):
    username = fields.Str(required=True, validate = [vns, Length(5, 10)])
    password = fields.Str(required=True, validate = vp)
    email = fields.Email(required=True)
    profiles_id = fields.Int(required=True)
    first_name = fields.Str(required=True)
    last_name = fields.Str(required=True)
    gender_id = fields.Int(required=True)
    city_id = fields.Int(required=True)

