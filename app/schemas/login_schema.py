from marshmallow import Schema
from marshmallow.fields import Email, Str


class LoginSchema(Schema):
    email = Email(
        required=True, error_messages={'required': 'Campo obrigatório'}
    )
    password = Str(
        required=True, error_messages={'required': 'Campo obrigatório'}
    )
