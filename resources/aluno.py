from flask_restful import Resource, reqparse, current_app, marshal, marshal_with
from sqlalchemy import exc
from helpers.database import db

from model.aluno import Aluno, aluno_fields
from model.endereco import Endereco
from model.error import Error, error_campos


parser = reqparse.RequestParser()
parser.add_argument('nome', required=True)
parser.add_argument('nascimento', required=True)
parser.add_argument('email', required=True)
parser.add_argument('senha', required=True)
parser.add_argument('telefone', required=True)
parser.add_argument('instituicaoDeEnsino', required=True)
parser.add_argument('curso', required=True)
parser.add_argument('matricula', required=True)
parser.add_argument('endereco',type=dict, required=True)


class Alunos(Resource):
    @marshal_with(aluno_fields)
    
    def get(self):
        current_app.logger.info("Get - Alunos")
        aluno = Aluno.query\
            .all()
        return aluno, 200

    def post(self):
        current_app.logger.info("Post - Alunos")
        try:
            # JSON
            args = parser.parse_args()
            nome = args['nome']
            nascimento = args['nascimento']
            email = args['email']
            senha = args['senha']
            telefone = args['telefone']        
            instituicaoDeEnsino = args['instituicaoDeEnsino']
            curso = args['curso']                    
            matricula = args['matricula']
            #Endereco
            cep = args['endereco']['cep']
            numero = args['endereco']['numero']
            complemento = args['endereco']['complemento']
            referencia = args['endereco']['referencia']
            logradouro = args['endereco']['logradouro']
            endereco = Endereco(cep, numero, complemento,
                                referencia, logradouro)


            # Aluno
            cadastro = Aluno(nome, nascimento, email,senha, telefone, instituicaoDeEnsino, curso, matricula, endereco)
            # Criação do Cadastro de aluno.
            db.session.add(cadastro)
            db.session.commit()
        except exc.SQLAlchemyError as err:
            current_app.logger.error(err)
            erro = Error(1, "Erro ao adicionar no banco de dados, consulte o adminstrador",
                         err.__cause__())
            return marshal(erro, error_campos), 500

        return 204


class AlunoResource(Resource):    
    def put(self, id):
        current_app.logger.info("Put - Alunos")
        try:
         # Parser JSON
            args = parser.parse_args()
            current_app.logger.info("ALuno: %s:" % args)
            nome = args['nome']
            nascimento = args['nascimento']
            email = args['email']
            senha = args['senha']
            telefone = args['telefone']        
            instituicaoDeEnsino = args['instituicaoDeEnsino']
            curso = args['curso']                    
            matricula = args['matricula']
            #Endereco
            cep = args['endereco']['cep']
            numero = args['endereco']['numero']
            complemento = args['endereco']['complemento']
            referencia = args['endereco']['referencia']
            logradouro = args['endereco']['logradouro']
            endereco = Endereco(cep, numero, complemento,
                                referencia, logradouro)

            aluno =Aluno.query \
                .filter_by(id=id) \
                .update(dict(nome = nome, nascimento = nascimento, email = email, senha=senha, telefone=telefone,
                 instituicaoDeEnsino=instituicaoDeEnsino, curso=curso, matricula=matricula, endereco=endereco))

            db.session.commit()
            #     .first()

            # aluno.nome = nome
            # aluno.nascimento = nascimento
            # aluno.email = email
            # aluno.senha = senha
            # aluno.telefone = telefone
            # aluno.instituicaoDeEnsino = instituicaoDeEnsino
            # aluno.curso = curso
            # aluno.matricula = matricula
            # aluno.endereco.cep = cep
            # aluno.endereco.numero = numero
            # aluno.endereco.complemento = complemento
            # aluno.endereco.referencia = referencia
            # aluno.endereco.logradouro = logradouro

            

        except exc.SQLAlchemyError:
            current_app.logger.error("Exceção")

        return 204