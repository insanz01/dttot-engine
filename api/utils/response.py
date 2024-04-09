from flask import make_response, jsonify
from .error_codes import ERROR_CODE_UNAUTHORIZED

JSON_MIME_TYPE = 'application/json'


def error(code, message):
    return {
        'code': code,
        'error': message
    }


def json_response(data=None, status=200, headers=None):
    headers = headers or {}
    if 'Content-Type' not in headers:
        headers['Content-Type'] = JSON_MIME_TYPE

    if data:
        payload = jsonify(data)
    else:
        payload = ''

    return make_response(payload, status, headers)


def response_success(data=None, status=200):
    return json_response(data=data, status=status)


def response_error(message, status=400):
    return json_response(data=error(status, message), status=status)


def response_not_authorized():
    return response_error("Unauthorized", ERROR_CODE_UNAUTHORIZED)
