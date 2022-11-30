from model.passageiro import Passageiro,passageiro_fields
from model.error import Error, error_campos
from helpers.database import db
from flask import jsonify
from sqlalchemy import exc
from flask_restful import Resource, marshal_with, reqparse, current_app, marshal

parser = reqparse.RequestParser()
parser.add_argument('nome', required=True)
parser.add_argument('cidadeOrigem', required=True)
parser.add_argument('cidadeDestino', required=True)

class Passageiros(Resource):
    @marshal_with(passageiro_fields)
    def get(self):
        current_app.logger.info("Get - Passageiro")
        passageiro = Passageiro.query\
            .order_by(Passageiro.nome)\
            .all()
        return passageiro, 200
    def post(self):
        current_app.logger.info("Post - Passageiros")
        try:
            # JSON
            args = parser.parse_args()
            nome = args['nome']
            cidadeOrigem = args['cidadeOrigem']
            cidadeDestino = args['cidadeDestino']
            # Passageiro
            passageiro = Passageiro(nome,cidadeOrigem,cidadeDestino)
            # Criação do Passageiro.
            db.session.add(passageiro)
            db.session.commit()
        except exc.SQLAlchemyError as err:
            current_app.logger.error(err)
            erro = Error(1, "Erro ao adicionar no banco de dados, consulte o adminstrador",
                         err.__cause__())
            return marshal(erro, error_campos), 500

        return 204
    
    def put(self, passageiro_id):
        current_app.logger.info("Put - Passageiros")
        try:
            # Parser JSON
            args = parser.parse_args()
            current_app.logger.info("Passageiro: %s:" % args)
            # Evento
            nome = args['nome']
            cidadeOrigem = args['cidadeOrigem']
            cidadeDestino = args['cidadeDestino']

            Passageiro.query \
                .filter_by(id=passageiro_id) \
                .update(dict(nome=nome,cidadeOrigem = cidadeOrigem,cidadeDestino = cidadeDestino ))
            db.session.commit()

        except exc.SQLAlchemyError:
            current_app.logger.error("Exceção")

        return 204
    
    def delete(self, passageiro_id):
        current_app.logger.info("Delete - Passageiros: %s:" % passageiro_id)
        try:
            Passageiro.query.filter_by(id=passageiro_id).delete()
            db.session.commit()

        except exc.SQLAlchemyError:
            current_app.logger.error("Exceção")
            return 404

        return 204