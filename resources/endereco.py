from flask_restful import Resource, reqparse, current_app, marshal, marshal_with
from sqlalchemy import exc

from helpers.database import db

from model.error import Error, error_campos

from model.endereco import Endereco, endereco_fields


parser = reqparse.RequestParser()
parser.add_argument('cep', required=True)
parser.add_argument('numero', required=True)
parser.add_argument('complemento', required=True)
parser.add_argument('referencia', required=True)
parser.add_argument('logradouro', required=True)
parser.add_argument('cidade', required=True)


class Enderecos(Resource):
    @marshal_with(endereco_fields)
    def get(self):
        current_app.logger.info("Get - Endereços")
        endereco = Endereco.query\
            .all()
        return endereco, 200

    @marshal_with(endereco_fields)
    def post(self):
        current_app.logger.info("Post - Endereços")
        try:
            # JSON
            args = parser.parse_args()
            cep = args['cep']
            numero = args['numero']
            complemento = args['complemento']
            referencia = args['referencia']
            logradouro = args['logradouro']
            cidade = args['cidade']

            # Endereco
            endereco = Endereco(cep, numero, complemento, referencia, logradouro, cidade)
            # Criação do Endereco.
            db.session.add(endereco)
            db.session.commit()
            
        except exc.SQLAlchemyError as err:
            current_app.logger.error(err)
            erro = Error(1, "Erro ao adicionar no banco de dados, consulte o adminstrador",
                         err.__cause__())
            return marshal(erro, error_campos), 500

        return 204

    @marshal_with(endereco_fields)
    def put(self, endereco_id):
        current_app.logger.info("Put - Endereço")
        try:
            # Parser JSON
            args = parser.parse_args()
            current_app.logger.info("Endereço: %s:" % args)
            # Evento
            cep = args['cep']
            numero = args['numero']
            complemento = args['complemento']
            referencia = args['referencia']
            logradouro = args['logradouro']
            cidade = args['cidade']

            Endereco.query \
                .filter_by(id=endereco_id) \
                .update(dict(cep=cep, numero=numero, complemento=complemento, referencia=referencia, logradouro=logradouro, cidade=cidade))
            db.session.commit()

        except exc.SQLAlchemyError:
            current_app.logger.error("Exceção")

        return 204

    @marshal_with(endereco_fields)
    def delete(self, endereco_id):
        current_app.logger.info("Delete - Endereço: %s:" % endereco_id)
        try:
            Endereco.query.filter_by(id=endereco_id).delete()
            db.session.commit()

        except exc.SQLAlchemyError:
            current_app.logger.error("Exceção")
            return 404

        return 204
