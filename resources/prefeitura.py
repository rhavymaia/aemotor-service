from flask import jsonify
from model.error import Error, error_campos
from sqlalchemy import exc
from helpers.database import db
from flask_restful import Resource, marshal_with, reqparse, current_app, marshal
from model.prefeitura import Prefeitura

parser = reqparse.RequestParser()
parser.add_argument('nomePrefeito', required=True)
parser.add_argument('email', required=True)
parser.add_argument('secretarios', required=True)
parser.add_argument('telefone', required=True)

class Prefeituras(Resource):
    def get(self):
        current_app.logger.info("Get - Prefeituras ")
        prefeitura = Prefeitura.query\
            .order_by(Prefeitura.email)\
            .all()
        return prefeitura, 200
    
    def post(self):
        current_app.logger.info("Post - Prefeitura")
        try:
            # JSON
            args = parser.parse_args()
            nomePrefeito = args['nomePrefeito']
            email = args['email']
            secretarios = args['secretarios']
            telefone = args['telefone']
            # Prefeitura
            prefeitura = Prefeitura(nomePrefeito,email,secretarios,telefone)
            # Criação do Prefeitura.
            db.session.add(prefeitura)
            db.session.commit()
        except exc.SQLAlchemyError as err:
            current_app.logger.error(err)
            erro = Error(1, "Erro ao adicionar no banco de dados, consulte o adminstrador",
                         err.__cause__())
            return marshal(erro, error_campos), 500

        return 204
    
    def put(self, prefeitura_id):
        current_app.logger.info("Put - Prefeitura")
        try:
            # Parser JSON
            args = parser.parse_args()
            current_app.logger.info("Prefeitura: %s:" % args)
            # Event
            nomePrefeito = args['nomePrefeito']
            email = args['email']
            secretarios = args['secretarios']
            telefone = args['telefone']
            Prefeitura.query \
                .filter_by(id=prefeitura_id) \
                .update(dict(nomePrefeito=nomePrefeito,email=email,secretarios=secretarios,telefone=telefone))
            db.session.commit()

        except exc.SQLAlchemyError:
            current_app.logger.error("Exceção")

        return 204
    
    def delete(self, prefeitura_id):
        current_app.logger.info("Delete - Prefeitura: %s:" % prefeitura_id)
        try:
            Prefeitura.query.filter_by(id=prefeitura_id).delete()
            db.session.commit()

        except exc.SQLAlchemyError:
            current_app.logger.error("Exceção")
            return 404

        return 204