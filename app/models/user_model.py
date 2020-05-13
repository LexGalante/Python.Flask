from app.db import db
from datetime import datetime
from mongoengine import StringField
from mongoengine import BooleanField
from mongoengine import EmailField
from mongoengine import DateTimeField
from mongoengine import EmbeddedDocument
from mongoengine import EmbeddedDocumentListField
from mongoengine import ListField


class User(db.Document):
    meta = {
        'collection': 'users',
        'ordering': ['email']
    }

    name = StringField(required=True)
    email = EmailField(required=True, unique=True)
    password = StringField(required=True)
    created_at = DateTimeField(default=datetime.now)
    updated_at = DateTimeField(default=datetime.now)
    active = BooleanField(default=False)
    roles = ListField(StringField(max_length=100), default=[])
