from flask_restful import Resource, reqparse, current_app, marshal, marshal_with
from sqlalchemy import exc

from helpers.database import db

from model.aluno import Aluno
from model.endereco import Endereco
from model.error import Error, error_campos


parser = reqparse.RequestParser()
parser.add_argument('nome', required=True)
parser.add_argument('nascimento', required=True)
parser.add_argument('email', required=True)
parser.add_argument('telefone', required=True)
parser.add_argument('instituicaoDeEnsino', required=True)
parser.add_argument('curso', required=True)
parser.add_argument('matricula', required=True)
#parser.add_argument('endereco', required=True)
class cadastroEstudantes(Resource):
    def get(self):
        current_app.logger.info("Get - Endereços")
        endereco = Aluno.query\
            .all()
        return endereco, 200

    def post(self):
        current_app.logger.info("Post - Endereços")
        try:
            # JSON
            args = parser.parse_args()
            nome = args['nome']
            nascimento = args['nascimento']
            email = args['email']
            telefone = args['telefone']        
            instituicaoDeEnsino = args['instituicaoDeEnsino']
            curso = args['curso']                    
            matricula = args['matricula']
            # Endereco
            #cep = args['endereco']['cep']
            # numero = args['endereco']['numero']
            # complemento = args['endereco']['complemento']
            # referencia = args['endereco']['referencia']
            # logradouro = args['endereco']['logradouro']
            # endereco = Endereco(numero, complemento,
            #                     referencia, logradouro)

            # Endereco
            cadastro = Aluno(nome, nascimento, email, telefone, instituicaoDeEnsino, curso, matricula)
            # Criação do Endereco.
            db.session.add(cadastro)
            db.session.commit()
        except exc.SQLAlchemyError as err:
            current_app.logger.error(err)
            erro = Error(1, "Erro ao adicionar no banco de dados, consulte o adminstrador",
                         err.__cause__())
            return marshal(erro, error_campos), 500

        return 204
