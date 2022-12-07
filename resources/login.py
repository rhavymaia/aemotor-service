
from flask_restful import Resource, reqparse, current_app, marshal, marshal_with
from sqlalchemy import exc

from helpers.database import db
from model.pessoa import Pessoa, pessoa_fields
from model.error import Error, error_campos


parser = reqparse.RequestParser()
parser.add_argument('email', required=True, help="Campo Email é obrigatório!")
parser.add_argument('senha', required=True, help="Campo Senha é obrigatório!")


class Login(Resource):
    @marshal_with(pessoa_fields)
    def post(self):
        current_app.logger.info("Post - Login")
        try:
            # JSON
            args = parser.parse_args()
            email = args['email']
            senha = args['senha']

            usuario = Pessoa.query.filter_by(email=email, senha=senha).first()

            if usuario is None:
                return 401
            else:
                return 200

        except exc.SQLAlchemyError as err:

            current_app.logger.error(err)
            erro = Error(1, "Erro ao adicionar no banco de dados, consulte o adminstrador",
                         err.__cause__())
            return marshal(erro, error_campos), 500

        return 200