from model.aluno import Aluno,aluno_fields
from model.error import Error, error_campos
from helpers.database import db
from flask import jsonify
from sqlalchemy import exc
from flask_restful import Resource, marshal_with, reqparse, current_app, marshal
from model.endereco import Endereco
from model.cidade import Cidade
from model.uf import Uf

parser = reqparse.RequestParser()
parser.add_argument('nome', required=True)
parser.add_argument('nascimento', required=True)
parser.add_argument('email', required=True)
parser.add_argument('senha', required=True,
                    help="Senha é campo obrigatório.")
parser.add_argument('telefone', required=True)
parser.add_argument('endereco', type=dict, required=True)
parser.add_argument('instituicaoDeEnsino', required=True)
parser.add_argument('curso', required=True)
parser.add_argument('matricula', required=True)

class AlunosResource(Resource):
    @marshal_with(aluno_fields)
    def get(self):
        current_app.logger.info("Get - Alunodb")
        aluno = Aluno.query\
            .order_by(Aluno.curso)\
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
             # Endereco
            enderecoArgs = args['endereco']
            cep = enderecoArgs['cep']
            numero = enderecoArgs['numero']
            complemento = enderecoArgs['complemento']
            referencia = enderecoArgs['referencia']
            logradouro = enderecoArgs['logradouro']
            
            # Cidade
            cidade = enderecoArgs['cidade']
            nomeCidade = cidade['nome']
            siglaCidade = cidade['sigla']
            
            #Uf
            uf = cidade['uf']
            nomeUf = uf['nome']
            siglaUf = uf['sigla']


            cidade = Cidade(nomeCidade, siglaCidade, Uf(nomeUf, siglaUf))
            endereco = Endereco(cep, numero, complemento,
                                referencia, logradouro, cidade)
            # Alunodb
            aluno = Aluno(nome, nascimento, email, senha, telefone, endereco,instituicaoDeEnsino,curso,matricula)
            # Criação do Alunodb.
            db.session.add(aluno)
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
            # JSON
            args = parser.parse_args()
            nome = args['nome']
            nascimento = args['nascimento']
            email = args['email']
            senha = args['senha']
            telefone = args['telefone']

            # Endereco
            enderecoArgs = args['endereco']
            cep = enderecoArgs['cep']
            numero = enderecoArgs['numero']
            complemento = enderecoArgs['complemento']
            referencia = enderecoArgs['referencia']
            logradouro = enderecoArgs['logradouro']
            # Cidade
            cidadeArgs = enderecoArgs['cidade']
            nomeCidade = cidadeArgs['nome']
            siglaCidade = cidadeArgs['sigla']

            # UF
            ufArgs = cidadeArgs['uf']
            nomeUf = ufArgs['nome']
            siglaUf = ufArgs['sigla']
            
            instituicaoDeEnsino = args['instituicaoDeEnsino']
            curso = args['curso']
            matricula = args['matricula']

            aluno =Aluno.query \
                .filter_by(id=id) \
                .first()

            aluno.nome = nome
            aluno.nascimento = nascimento
            aluno.email = email
            aluno.senha = senha
            aluno.telefone = telefone
            aluno.instituicaoDeEnsino = instituicaoDeEnsino
            aluno.curso = curso
            aluno.matricula = matricula
            aluno.endereco.cep = cep
            aluno.endereco.numero = numero
            aluno.endereco.complemento = complemento
            aluno.endereco.referencia = referencia
            aluno.endereco.logradouro = logradouro
            aluno.endereco.cidade.nome = nomeCidade
            aluno.endereco.cidade.sigla = siglaCidade
            aluno.endereco.cidade.uf.nome = nomeUf
            aluno.endereco.cidade.uf.sigla = siglaUf

            db.session.commit()

        except exc.SQLAlchemyError:
            current_app.logger.error("Exceção")

        return 204
    
    def delete(self, id):
        current_app.logger.info("Delete - Alunodb: %s:" % id)
        try:
            Aluno.query.filter_by(id=id).delete()
            db.session.commit()

        except exc.SQLAlchemyError:
            current_app.logger.error("Exceção")
            return 404

        return 204