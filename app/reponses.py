from flask import jsonify
from flask import Response


def ok(message="Sucesso", data={}):
    """HTTP Response 200"""
    response = jsonify({
        'status': True,
        'message': message,
        'data': data
    })
    response.status_code = 200

    return response


def created(message="", data={}):
    """HTTP Response 201"""
    response = jsonify({
        'status': True,
        'message': message,
        'data': data
    })
    response.status_code = 200

    return response


def no_content():
    """HTTP Response 204"""
    return Response(status=204)


def bad_request(message='Ocorreram erros verifique', errors={}):
    """HTTP Response 400"""
    response = jsonify({
        'status': False,
        'message': message,
        'data': errors
    })
    response.status_code = 400

    return response


def unathorized():
    """HTTP Response 401"""
    response = jsonify({
        'status': False,
        'message': 'Sem autorização',
    })
    response.status_code = 401

    return response


def error(message='Ocorreu um erro inesperado', e=None):
    """HTTP Response 500"""
    response = jsonify({
        'status': False,
        'message': message,
        'data': e
    })
    response.status_code = 500

    return response
