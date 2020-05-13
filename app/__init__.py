from flask import Flask
from config import config
from app.api import configure_api
from app.db import configure_db
from app.jwt import configure_jwt


# configurações do flask
def create_app(config_name):
    # configurações do Flask
    app = Flask(__name__)
    # injetando as váriaves de configuração do Flask
    app.config.from_object(config[config_name])
    # configurações flask_restul
    configure_api(app)
    # configurações jwt
    configure_jwt(app)
    # configurações mongengine
    configure_db(app)

    return app
