from model.endereco import endereco_fields
from flask_restful import fields
from helpers.database import db
from sqlalchemy.types import String

pessoa_fields = {
    'id': fields.Integer(attribute='id'),
    'nome': fields.String(attribute='nome'),
    'nascimento': fields.String(attribute='nascimento'),
    'email': fields.String(attribute='email'),
    'telefone': fields.String(attribute='telefone'),
    'endereco': fields.Nested(endereco_fields)
}
class Pessoa(db.Model):

    __tablename__ = "tb_pessoa"

 
    id = db.Column('id', db.Integer, primary_key=True)
    nome = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String(200), unique=True)
    telefone = db.Column(db.String(11))
    nascimento = db.Column(db.Date) 
   
    aluno = db.relationship("Aluno", uselist=False)
    prefeito = db.relationship("Prefeito", uselist=False)
    endereco = db.relationship("Endereco", uselist=False)
    funcionario = db.relationship("Funcionario", uselist=False)
    gestor = db.relationship("GestorApp", uselist=False)

    # Herança: Superclasse

    
    def __init__(self, nome, nascimento, email, telefone, endereco):
        self.nome = nome
        self.nascimento = nascimento
        self.email = email
        self.telefone = telefone
        self.endereco = endereco

    def __repr__(self):
        return '<Nome: {}\n Data de Nascimento: {}\n Email: {}\n Telefone: {}>'.format(self.nome, self.nascimento, self.email, self.telefone)
