from flask_restful import Resource, reqparse, current_app, marshal, marshal_with
from sqlalchemy import exc

from flask_restful import Resource

parser = reqparse.RequestParser()
parser.add_argument('email', required=True)
parser.add_argument('senha', required=True)


class Login(Resource):

    def post(self):
        current_app.logger.info("Post - Login")

        # JSON
        args = parser.parse_args()
        email = args['email']
        senha = args['senha']
        # TODO - Adicionar consulta ao banco de dados.

        return 200
