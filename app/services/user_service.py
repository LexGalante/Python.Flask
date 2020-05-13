
from app.models.user_model import User
from bcrypt import gensalt
from bcrypt import hashpw
from bcrypt import checkpw


def get_users(page: int, page_size: int):
    """Retorna os usuário, pode realizar paginação se receber page e page_size"""
    if page is None or page is 0:
        return User.objects()
    return User.objects().paginate(page, page_size)


def get_user_by_email(email: str) -> User:
    """Busca o usuário por seu email"""
    return User.objects(email=email).first()


def create_user(json: dict) -> User:
    """Salva um novo usuário baseado em dicionário"""
    json["password"] = hashpw(json["password"].encode('utf-8'), gensalt(12))
    model = User(**json)
    model.save()
    del model.password
    return model


def update_user(email: str, json: dict) -> User:
    user = User.objects(email=email).first()
    if user is None:
        raise ValueError(f'Usuário {email} não encontrado')
    if "email" in json.keys():
        del json["email"]
    if "password" in json.keys():
        del json["password"]

    for key, value in json.items():
        user[key] = value
    user.save()


def delete_user(email: str):
    User.objects(email=email).delete()


def validate_password(user: User, password: str) -> bool:
    return checkpw(password.encode('utf-8'), user.password.encode('utf-8'))
