
from flask_restful import Resource, reqparse, current_app, marshal, marshal_with
from sqlalchemy import exc

from helpers.database import db

from model.endereco import Endereco_db
from model.error import Error, error_campos


parser = reqparse.RequestParser()
parser.add_argument('cep', required=True)
parser.add_argument('complemento', required=True)
parser.add_argument('referencia', required=True)
parser.add_argument('logradouro', required=True)


class Endereco(Resource):
    def get(self):
        current_app.logger.info("Get - Endereços")
        endereco = Endereco_db.query\
            .all()
        return endereco, 200

    def post(self):
        current_app.logger.info("Post - Endereços")
        try:
            # JSON
            args = parser.parse_args()
            cep = args['cep']
            complemento = args['complemento']
            referencia = args['referencia']
            logradouro = args['logradouro']

            # Enderecodb
            endereco = Endereco_db(cep,complemento,referencia,logradouro)
            # Criação do Enderecodb.
            db.session.add(endereco)
            db.session.commit()
        except exc.SQLAlchemyError as err:
            current_app.logger.error(err)
            erro = Error(1, "Erro ao adicionar no banco de dados, consulte o adminstrador",
                         err.__cause__())
            return marshal(erro, error_campos), 500

        return 204

    def put(self, endereco_id):
        current_app.logger.info("Put - Endereço")
        try:
            # Parser JSON
            args = parser.parse_args()
            current_app.logger.info("Endereço: %s:" % args)
            # Evento
            cep = args['cep']
            complemento = args['complemento']
            referencia = args['referencia']
            logradouro = args['logradouro']
            Endereco_db.query \
                .filter_by(id=endereco_id) \
                .update(dict(cep=cep,complemento=complemento,referencia=referencia,logradouro=logradouro))
            db.session.commit()

        except exc.SQLAlchemyError:
            current_app.logger.error("Exceção")

        return 204

    def delete(self, endereco_id):
        current_app.logger.info("Delete - Endereço: %s:" % endereco_id)
        try:
            Endereco_db.query.filter_by(id=endereco_id).delete()
            db.session.commit()

        except exc.SQLAlchemyError:
            current_app.logger.error("Exceção")
            return 404

        return 204