
from flask import request
from flask_restful import Resource, reqparse, current_app, marshal, marshal_with
from sqlalchemy import exc

from helpers.database import db
from model.instituicaoEnsino import instituicaoEnsino, instituicao_fields
from model.error import Error, error_campos

parser = reqparse.RequestParser()

endereco = parser.add_argument("endereco", required=True)
telefone = parser.add_argument("telefone", required=True)
nome = parser.add_argument("nome", required=True)

class InstituicoesEnsino(Resource):
    def get(self):
        current_app.logger.info("Get - Instituições de Ensino")
        endereco = instituicaoEnsino.query\
            .all()
        return endereco, 200

    def post(self):
        current_app.logger.info("Post - Instituições de Ensino")
        try:
            # JSON
            args = parser.parse_args()
            endereco = args['endereco']
            telefone = args['telefone']
            nome = args['nome']

            # Endereco
            instituicao = instituicaoEnsino(endereco, telefone, nome)
            # Criação do Endereco.
            db.session.add(instituicao)
            db.session.commit()
            
        except exc.SQLAlchemyError as err:
            current_app.logger.error(err)
            erro = Error(1, "Erro ao adicionar no banco de dados, consulte o adminstrador",
                         err.__cause__())
            return marshal(erro, error_campos), 500

        return 204