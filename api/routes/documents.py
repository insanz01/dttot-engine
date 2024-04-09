from flask import Blueprint
from flask_restful import Api
from ..handler.documents import DocumentsAPI, TestAPI

DOCUMENTS_BLUEPRINT = Blueprint('documents', __name__)
Api(DOCUMENTS_BLUEPRINT).add_resource(TestAPI, '/test/')
Api(DOCUMENTS_BLUEPRINT).add_resource(DocumentsAPI, '/documents/')