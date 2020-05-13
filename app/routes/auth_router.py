from flask import request
from flask_restful import Resource
from flask_jwt_extended import create_access_token
from flask_jwt_extended import create_refresh_token
from flask_jwt_extended import jwt_refresh_token_required
from flask_jwt_extended import get_jwt_identity
from marshmallow.exceptions import ValidationError as SchemaValidationError
from app.reponses import bad_request
from app.reponses import ok
from app.reponses import error
from app.schemas.login_schema import LoginSchema
from app.services.user_service import get_user_by_email
from app.services.user_service import validate_password


class AuthRouter(Resource):
    def post(self, *args, **kwargs):
        json = request.get_json() or None
        if json is None:
            return bad_request('Dados da requisição inválidos')
        try:
            data = LoginSchema().load(json)
            user = get_user_by_email(data["email"])
            if not user.active:
                return bad_request(f'Usuário: {data["email"]} invativo')
            if not validate_password(user, data["password"]):
                return bad_request(f'Usuário ou senha inválidas')
            jwt = {
                'token': create_access_token(identity=user.email),
                'refresh': create_refresh_token(identity=user.email)
            }
            return ok(data=jwt)
        except SchemaValidationError as e:
            return bad_request('Requisição inválida', e.messages)
        except:
            return error()


class AuthRefreshRouter(Resource):
    @jwt_refresh_token_required
    def post(self, *args, **kwargs):
        user = get_jwt_identity()
        return ok(data={'token': create_access_token(identity=user)})
