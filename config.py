# -*- coding: utf-8 -*-

# Python
from os import getenv
from datetime import timedelta


class Config:
    SECRET_KEY = getenv('SECRET_KEY')
    APP_PORT = int(getenv('APP_PORT'))
    DEBUG = eval(getenv('DEBUG'))
    MONGODB_HOST = getenv('MONGODB_URI')
    JSON_AS_ASCII = eval(getenv('JSON_AS_ASCII'))
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(
        minutes=int(getenv('JWT_ACCESS_TOKEN_EXPIRES'))
    )
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(
        days=int(getenv('JWT_REFRESH_TOKEN_EXPIRES'))
    )


class Testing(Config):
    FLASK_ENV = 'testing'
    TESTING = True


class Development(Config):
    FLASK_ENV = 'development'
    DEBUG = True


config = {
    'testing': Testing,
    'development': Development,
    'default': Development
}
