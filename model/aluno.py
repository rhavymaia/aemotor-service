from model.pessoa import Pessoa
from model.endereco import endereco_fields,Endereco
from helpers.database import db
from sqlalchemy import ForeignKey
from flask_restful import fields

aluno_fields = {
    'id': fields.Integer(attribute='id'),
    'nome': fields.String(attribute='nome'),
    'nascimento': fields.String(attribute='nascimento'),
    'email': fields.String(attribute='email'),
    'telefone': fields.String(attribute='telefone'),
    'instituicaoDeEnsino': fields.String(attribute='instituicaoDeEnsino'),
    'curso': fields.String(attribute='curso'),
    'matricula': fields.String(attribute='matricula'),
    'endereco': fields.Nested(endereco_fields)
}

class Aluno(Pessoa, db.Model):

    __tablename__ = "tb_aluno"
    __mapper_args__ = {'polymorphic_identity': 'aluno'}

    id = db.Column(ForeignKey("tb_pessoa.id"), primary_key=True)
    instituicaoDeEnsino = db.Column(db.String, nullable=False)
    curso = db.Column(db.String, nullable=False)
    matricula = db.Column(db.String, unique=True, nullable=False)

    def __init__(self, nome, nascimento, email, senha, telefone,endereco, instituicaoDeEnsino, curso, matricula):
        super().__init__(nome, nascimento, email, senha,  telefone, endereco)
        self.instituicaoDeEnsino = instituicaoDeEnsino
        self.curso = curso
        self.matricula = matricula

    def __repr__(self):
        return '<Instituição de ensino: {}\n Curso: {}\n Matrícula: {}>'.format(self.instituicaoDeEnsino, self.curso, self.matricula)
