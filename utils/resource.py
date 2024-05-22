from flask_restful import Resource

from utils.dc import exception_wrap
from flask_jwt_extended import jwt_required


class Api(Resource):

    method_decorators = [exception_wrap]
