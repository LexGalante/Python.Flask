# -*- coding: utf-8 -*-
from marshmallow import Schema
from marshmallow.fields import Email
from marshmallow.fields import Str
from marshmallow.fields import DateTime
from marshmallow.fields import Boolean
from marshmallow.fields import List


class UserPostSchema(Schema):
    name = Str(required=True, error_messages={'required': 'Campo obrigatório'})
    email = Email(required=True, error_messages={
                  'required': 'Campo obrigatório'})
    password = Str(required=True, error_messages={
                   'required': 'Campo obrigatório'})
    active = Boolean(required=True, error_messages={
                     'required': 'Campo obrigatório'})
    roles = List(Str(maxlenght=100), required=True, error_messages={
                 'required': 'Campo obrigatório'})


class UserPutSchema(Schema):
    name = Str(required=True, error_messages={'required': 'Campo obrigatório'})
    active = Boolean(required=True, error_messages={
                     'required': 'Campo obrigatório'})
    roles = List(Str(maxlenght=100), required=True, error_messages={
                 'required': 'Campo obrigatório'})
