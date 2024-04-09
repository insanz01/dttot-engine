from flask_restful import Resource
from flask import request
from ..utils import parse_params
from ..utils.error_codes import ERROR_METHOD_NOT_ALLOWED, ERROR_BAD_REQUEST
from ..utils.permission import allowed_file
from ..utils.response import response_error, response_success
from werkzeug.utils import secure_filename


class DocumentsAPI(Resource):

    @staticmethod
    def post():
        if request.method != 'POST':
            return response_error('METHOD NOT SUPPORT', ERROR_METHOD_NOT_ALLOWED)

        if 'file'not in request.files:
            return response_error('FILE NOT FOUND', ERROR_BAD_REQUEST)

        file = request.files['file']

        if file.filename == '':
            return response_error('FILE NOT FOUND', ERROR_BAD_REQUEST)

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            print(filename)
            # TODO: save to bucket

class TestAPI(Resource):
    @staticmethod
    def get():
        data = {
            'test': 'test',
            'name': 'vika',
            'husband': 'the only god knows'
        }
        return response_success(data)