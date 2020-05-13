from flask import Flask
from flask import request
from flask import jsonify
from flask_restful import Resource
from mongoengine.errors import NotUniqueError
from mongoengine.errors import ValidationError as MongoValidationError
from marshmallow.exceptions import ValidationError as SchemaValidationError
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from app.services.user_service import get_users
from app.services.user_service import create_user
from app.services.user_service import update_user
from app.services.user_service import delete_user
from app.schemas.user_schema import UserPostSchema
from app.schemas.user_schema import UserPutSchema
from app.reponses import ok
from app.reponses import bad_request
from app.reponses import error


class UserRouter(Resource):
    @jwt_required
    def get(self, page=1, page_size=10, *args, **kwargs):
        try:
            users = get_users(page, page_size)
            for user in users.items:
                del user.password

            return ok(data=users.items)
        except Exception as e:
            return error()

    @jwt_required
    def post(self, *args, **kwargs):
        json = request.get_json() or None

        if json is None:
            return bad_request('Dados da requisição inválidos')

        try:
            # deserialização
            data = UserPostSchema().load(json)
            user = create_user(data)
        except NotUniqueError:
            return bad_request('O email já está em uso!!!')
        except MongoValidationError as e:
            return bad_request('Error ao armazenar', e)
        except SchemaValidationError as e:
            return bad_request('Requisição inválida', e.messages)
        except Exception as e:
            return error(e)
        else:
            return ok("Sucesso!!!", data=user)

    @jwt_required
    def put(self, email, *args, **kwargs):
        json = request.get_json() or None

        if json is None:
            return bad_request('Dados da requisição inválidos')

        try:
            data = UserPutSchema().load(json)
            user = update_user(email, data)
        except ValueError as e:
            return bad_request(e)
        except NotUniqueError:
            return bad_request('O email já está em uso!!!')
        except MongoValidationError as e:
            return bad_request('Error ao armazenar', e)
        except SchemaValidationError as e:
            return bad_request('Requisição inválida', e.messages)
        except:
            return error()
        else:
            return ok("Sucesso!!!", data=user)

    @jwt_required
    def delete(self, email, *args, **kwargs):
        try:
            delete_user(email)
        except:
            return error()
        else:
            return ok()
