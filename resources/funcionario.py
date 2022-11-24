from model.funcionario import Funcionario,funcionario_fields
from model.error import Error, error_campos
from helpers.database import db
from flask import jsonify
from sqlalchemy import exc
from flask_restful import Resource, marshal_with, reqparse, current_app, marshal

from helpers.database import db
from model.endereco import Endereco
from model.error import Error, error_campos

parser = reqparse.RequestParser()
parser.add_argument('nome', required=True)
parser.add_argument('nascimento', required=True)
parser.add_argument('email', required=True)
parser.add_argument('telefone', required=True)
parser.add_argument('endereco', type=dict, required=True)
parser.add_argument('prefeitura', required=True)
parser.add_argument('cargo', required=True)


class Funcionarios(Resource):
    @marshal_with(funcionario_fields)
    def get(self):
        current_app.logger.info("Get - Funcionarios")
        funcionario = Funcionario.query\
            .order_by(Funcionario.cargo)\
            .all()
        return funcionario, 200
    def post(self):
        current_app.logger.info("Post - Funcionarios")
        try:
            # JSON
            args = parser.parse_args()
            nome = args['nome']
            nascimento = args['nascimento']
            email = args['email']
            telefone = args['telefone']
            #Endereco_db
            cep= args['endereco']['cep']
            numero = args['endereco']['numero']
            complemento = args['endereco']['complemento']
            referencia = args['endereco']['referencia']
            logradouro = args['endereco']['logradouro']
            endereco = Endereco(cep, numero, complemento,
                                referencia, logradouro)

            prefeitura = args['prefeitura']
            cargo = args['cargo']

            # Funcionario
            funcionario = Funcionario(
                nome, nascimento, email, telefone, endereco, prefeitura, cargo)
            # Criação do Funcionario.
            db.session.add(funcionario)
            db.session.commit()
        except exc.SQLAlchemyError as err:
            current_app.logger.error(err)
            erro = Error(1, "Erro ao adicionar no banco de dados, consulte o adminstrador",
                         err.__cause__())
            return marshal(erro, error_campos), 500

        return 204
    
    def put(self, funcionario_id):
        current_app.logger.info("Put - Funcionarios")
        try:
            # Parser JSON
            args = parser.parse_args()
            current_app.logger.info("Funcionario: %s:" % args)
            # Evento
            prefeitura = args['prefeitura']
            cargo = args['cargo']
    

            Funcionario.query \
                .filter_by(id=funcionario_id) \
                .update(dict(prefeitura=prefeitura,cargo = cargo ))
            db.session.commit()

        except exc.SQLAlchemyError:
            current_app.logger.error("Exceção")

        return 204
    
    def delete(self, funcionario_id):
        current_app.logger.info("Delete - Funcionarios: %s:" % funcionario_id)
        try:
            Funcionario.query.filter_by(id=funcionario_id).delete()
            db.session.commit()

        except exc.SQLAlchemyError:
            current_app.logger.error("Exceção")
            return 404

        return 204