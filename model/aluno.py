from model.pessoa import Pessoa
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
    'endereco': fields.String(attribute='endereco')
}

class Aluno(Pessoa, db.Model):

    __tablename__ = "tb_aluno"
    __mapper_args__ = {'polymorphic_identity': 'aluno'}

    #id = db.Column(db.Integer, primary_key=True)
    id = db.Column(ForeignKey("tb_pessoa.id"), primary_key=True)
    instituicaoDeEnsino = db.Column(db.String, nullable=False)
    curso = db.Column(db.String, nullable=False)
    matricula = db.Column(db.String, unique=True, nullable=False)

    
    endereco = db.relationship("Endereco", uselist=False)

    def __init__(self, nome, nascimento, email, senha, telefone, instituicaoDeEnsino, curso, matricula, endereco):
        super().__init__(nome, nascimento, email, senha, telefone, endereco)
        self.instituicaoDeEnsino = instituicaoDeEnsino
        self.curso = curso
        self.matricula = matricula
        self.endereco = endereco

    def __repr__(self):
        return '<Nome: {}\n Nascimento: {}\n Email: {}\n Telefone: {}\n Instituição de ensino: {}\n Curso: {}\n Matrícula: {}>'.format(self.nome, self.nascimento, self.email, self.telefone, self.instituicaoDeEnsino, self.curso, self.matricula)
