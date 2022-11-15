from flask_restful import Resource, reqparse, current_app, marshal, marshal_with
from sqlalchemy import exc

from helpers.database import db
from model.error import Error, error_campos

from model.prefeitura import Prefeitura
from .serializer import response_serializer_prefeitura

parser = reqparse.RequestParser()
parser.add_argument('nome', required=True, location= 'json')
parser.add_argument('endereco', required=True, location= 'json')
parser.add_argument('nomePrefeito', required=True, location= 'json')

class Prefeitura_Resource(Resource):
    def get(self):
        current_app.logger.info("Get - Prefeitura")
        prefeituras = Prefeitura.query.all()
        response = response_serializer_prefeitura(prefeituras)
        return response, 200
    
    def post(self):
        current_app.logger.info("Post - Prefeitura")
        try:
            # JSON
            args = parser.parse_args()
            nome = args['nome']
            endereco = args['endereco']
            nomePrefeito = args['nomePrefeito']

            # Prefeitura
            prefeitura = Prefeitura(nome, endereco, nomePrefeito)
            
            # Criação do Prefeitura.
            db.session.add(prefeitura)
            db.session.commit()
        except exc.SQLAlchemyError as err:
            current_app.logger.error(err)
            erro = Error(1, "Erro ao adicionar no banco de dados, consulte o adminstrador",
                         err.__cause__())
            return marshal(erro, error_campos), 500

        return 204
    
    def put(self, id):
        current_app.logger.info("Put - Prefeitura")
        try:
            # Parser JSON
            args = parser.parse_args()
            current_app.logger.info("Prefeitura: %s:" % args)
            
            # Evento
            nome = args['nome']
            endereco = args['endereco']
            nomePrefeito = args['nomePrefeito']

            Prefeitura.query \
                .filter_by(id = id) \
                .update(dict(nome = nome, endereco = endereco, nomePrefeito = nomePrefeito))
            db.session.commit()

        except exc.SQLAlchemyError:
            current_app.logger.error("Exceção")

        return 204
    
    def delete(self, id):
        current_app.logger.info("Delete - Prefeitura: %s:" % id)
        try:
            Prefeitura.query.filter_by(id=id).delete()
            db.session.commit()

        except exc.SQLAlchemyError:
            current_app.logger.error("Exceção")
            return 404

        return 204