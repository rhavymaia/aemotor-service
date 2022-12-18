from model.login import email, senha
from flask_restful import Resource, reqparse, current_app, marshal, marshal_with
from sqlalchemy import exc

from helpers.database import db
from model.login import Login, login_fields
from model.error import Error, error_campos

parser = reqparse.RequestParser()
parser.add_argument('email', required=True)
parser.add_argument('senha', required=True)

class Login(Resource):

    @marshal_with(login_fields)
    def get(self):
        
        current_app.logger.info("Get - Login")
        login_one = db.session.execute(db.select(Login).filter_by(email=email, senha=senha)).one()
        return login_one, 200

    # def post(self):
    #     current_app.logger.info("Post - Login")
    #     try:
    #         # JSON
    #         args = parser.parse_args()
    #         email = args['email']
    #         senha = args['senha']
    #         # Login
    #         _login = Login(
    #             email, senha)
    #         # Criação de Login.
    #         db.session.add(_login)
    #         db.session.commit()
    #     except exc.SQLAlchemyError as err:
    #         current_app.logger.error(err)
    #         erro = Error(1, "Erro ao adicionar no banco de dados, consulte o adminstrador",
    #                      err.__cause__())
    #         return marshal(erro, error_campos), 500

    #     return 204

    # def put(self):
    #     current_app.logger.info("Update - Login")
    #     email.verified = True
    #     db.session.commit()