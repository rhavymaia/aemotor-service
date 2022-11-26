
from flask_restful import Resource, reqparse, current_app, marshal, marshal_with
from sqlalchemy import exc

from helpers.database import db

from model.pessoa import Pessoa
from model.error import Error, error_campos


parser = reqparse.RequestParser()
parser.add_argument('email', required=True)
parser.add_argument('senha', required=True)


class Login(Resource):

    def post(self):
        current_app.logger.info("Post - Endereços")
        try:
            # JSON
            args = parser.parse_args()
            email = args['email']
            senha = args['senha']

            db.select(Pessoa).filter_by(email=email, senha=senha)

        except exc.SQLAlchemyError as err:
            current_app.logger.error(err)
            erro = Error(1, "Erro ao adicionar no banco de dados, consulte o adminstrador",
                         err.__cause__())
            return marshal(erro, error_campos), 500

        return 204