from flask_restful import Resource, reqparse, current_app, marshal, marshal_with
from sqlalchemy import exc

from helpers.database import db
from model.funcionario import Funcionario, funcionario_fields
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

'''
  Classe Funcionário.
'''


class Funcionarios(Resource):

    @marshal_with(funcionario_fields)
    def get(self):
        current_app.logger.info("Get - Funcionarios")
        funcionarios = Funcionario.query\
            .all()
        return funcionarios, 200

    def post(self):
        current_app.logger.info("Post - Funcionario")
        try:
            # JSON
            args = parser.parse_args()
            nome = args['nome']
            nascimento = args['nascimento']
            email = args['email']
            telefone = args['telefone']

            # Endereco
            cep = args['endereco']['cep']
            numero = args['endereco']['numero']
            complemento = args['endereco']['complemento']
            referencia = args['endereco']['referencia']
            logradouro = args['endereco']['logradouro']
            endereco = Endereco(cep, numero, complemento,
                                referencia, logradouro)

            prefeitura = args['prefeitura']
            cargo = args['cargo']

            # Funcionário
            funcionario = Funcionario(
                nome, nascimento, email, telefone, endereco, prefeitura, cargo)
            # Criação do Funcionário.
            db.session.add(funcionario)
            db.session.commit()
        except exc.SQLAlchemyError as err:
            current_app.logger.error(err)
            erro = Error(1, "Erro ao adicionar no banco de dados, consulte o adminstrador",
                         err.__cause__())
            return marshal(erro, error_campos), 500

        return 204
