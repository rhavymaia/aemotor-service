from model.pessoa import Pessoa_db
from model.endereco import endereco_fields
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

class Aluno(Pessoa_db,db.Model):
  
    
    __tablename__ = 'tb_aluno'
    __mapper_args__ = {'polymorphic_identity': 'aluno'}

    id_aluno = db.Column(ForeignKey("tb_pessoa.id"), primary_key=True)
    instituicaoDeEnsino = db.Column(db.String(80), nullable=False)
    curso = db.Column(db.String(50), nullable=False)
    matricula = db.Column(db.String(20), nullable=False) 
    
    instituicao_child = db.relationship("InstituicaoDeEnsino_db", uselist=False)
    rotas = db.relationship('Rota_db', backref='Rota_db', lazy=True)
    passageiro_child = db.relationship('Passageiro_db',uselist=False)
    

    def __init__(self, nome, nascimento, email, telefone,endereco, instituicaoDeEnsino, curso, matricula,pessoa):
        super().__init__(nome, nascimento, email, telefone,endereco)
        self.instituicaoDeEnsino = instituicaoDeEnsino
        self.curso = curso
        self.matricula = matricula
        
    
    def __repr__(self):
        return '\nNome:{}\n Nascimento: {}\n Email: {}\n Telefone: {}\n Instituto: {}\n Curso: {}\n Matrícula: {}'.format(self.nome, self.nascimento, self.email, self.telefone, self.instituicaoDeEnsino, self.curso, self.matricula)