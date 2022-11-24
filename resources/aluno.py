from model.aluno import Aluno,aluno_fields
from model.error import Error, error_campos
from helpers.database import db
from flask import jsonify
from sqlalchemy import exc
from flask_restful import Resource, marshal_with, reqparse, current_app, marshal
from model.endereco import Endereco_db

parser = reqparse.RequestParser()
parser.add_argument('nome', required=True)
parser.add_argument('nascimento', required=True)
parser.add_argument('email', required=True)
parser.add_argument('telefone', required=True)
parser.add_argument('endereco', type=dict, required=True)
parser.add_argument('instituicaoDeEnsino', required=True)
parser.add_argument('curso', required=True)
parser.add_argument('matricula', required=True)

class Alunos(Resource):
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
            telefone = args['telefone']
            instituicaoDeEnsino = args['instituicaoDeEnsino']
            curso = args['curso']
            matricula = args['matricula']
             #Endereco_db
            cep = args['endereco']['cep']
            numero = args['endereco']['numero']
            complemento = args['endereco']['complemento']
            referencia = args['endereco']['referencia']
            logradouro = args['endereco']['logradouro']
            endereco = Endereco_db(cep, numero, complemento,
                                referencia, logradouro)
            # Alunodb
            aluno = Aluno( nome, nascimento, email, telefone, endereco,instituicaoDeEnsino,curso,matricula)
            # Criação do Alunodb.
            db.session.add(aluno)
            db.session.commit()
        except exc.SQLAlchemyError as err:
            current_app.logger.error(err)
            erro = Error(1, "Erro ao adicionar no banco de dados, consulte o adminstrador",
                         err.__cause__())
            return marshal(erro, error_campos), 500

        return 204
    
    def put(self, aluno_id):
        current_app.logger.info("Put - Alunos")
        try:
            # Parser JSON
            args = parser.parse_args()
            current_app.logger.info("Alunodb: %s:" % args)
            # Evento
            instituicaoDeEnsino = args['instituicaoDeEnsino']
            curso = args['curso']
            matricula = args['matricula']

            Aluno.query \
                .filter_by(id=aluno_id) \
                .update(dict(instituicaoDeEnsino=instituicaoDeEnsino,curso = curso, matricula = matricula))
            db.session.commit()

        except exc.SQLAlchemyError:
            current_app.logger.error("Exceção")

        return 204
    
    def delete(self, aluno_id):
        current_app.logger.info("Delete - Alunodb: %s:" % aluno_id)
        try:
            Aluno.query.filter_by(id=aluno_id).delete()
            db.session.commit()

        except exc.SQLAlchemyError:
            current_app.logger.error("Exceção")
            return 404

        return 204