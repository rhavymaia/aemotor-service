
from flask_restful import Resource, reqparse, current_app, marshal, marshal_with
from sqlalchemy import exc

import hashlib
from datetime import datetime
from helpers.database import db
from model.pessoa import Pessoa
from model.login import Login, login_campos
from model.error import Error, error_campos


parser = reqparse.RequestParser()
parser.add_argument('email', required=True, help="Campo Email é obrigatório!")
parser.add_argument('senha', required=True, help="Campo Senha é obrigatório!")


class Login(Resource):
    def post(self):
        current_app.logger.info("Post - Login")
        print("foi...")
        try:
            # JSON
            args = parser.parse_args()
            email = args['email']
            senha = args['senha']

            #pessoa = Pessoa.query.filter_by(email=email, senha=senha).first()
            pessoa = Pessoa.query.filter_by(email=email, senha=senha).first()
            print(pessoa)
            
            if pessoa is not None:

                dataHoraLogin = datetime.now()
                hashlib.sha1().update(str(dataHoraLogin).encode("utf-8"))
                key = hashlib.sha1().hexdigest()

                login = Login(pessoa, dataHoraLogin, key)
                print(login)

                # Criação do Login.
                db.session.add(login)
                db.session.commit()

                return (marshal(login, login_campos), 200)
            else:
                return ({}, 401)

        except exc.SQLAlchemyError as err:

            current_app.logger.error(err)
            erro = Error(1, "Erro ao adicionar no banco de dados, consulte o adminstrador",
                         err.__cause__())
            return marshal(erro, error_campos), 500

        return 200