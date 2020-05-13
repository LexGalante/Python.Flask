from flask_mongoengine import MongoEngine


db = MongoEngine()

# configurações MongoDb


def configure_db(app):
    db.init_app(app)
