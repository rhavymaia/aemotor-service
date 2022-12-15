from helpers.database import db
from sqlalchemy.types import String
from flask_restful import fields
from model.endereco import Endereco, endereco_fields

pessoa_fields = {
    'id': fields.Integer(attribute='id'),
    'nome': fields.String(attribute='nome'),
    'nascimento': fields.String(attribute='nascimento'),
    'email': fields.String(attribute='email'),
    'senha': fields.String(attribute='senha'),
    'telefone': fields.String(attribute='telefone'),
    'endereco': fields.Nested(endereco_fields)
}

class Pessoa(db.Model):

    __tablename__ = "tb_pessoa"
    __tablename__ = "tb_pessoa"

    id = db.Column('id', db.Integer, primary_key=True)
    nome = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String(200), unique=True)
    senha = db.Column(db.String(300), unique=True,
                      nullable=False)
    telefone = db.Column(db.String(11))
    nascimento = db.Column(db.Date)
    # Relacionamento com Endereço
    endereco = db.relationship("Endereco", uselist=False)

    # Herança: Superclasse
    tipo_pessoa = db.Column('tipo_pessoa', String(50))
    __mapper_args__ = {'polymorphic_on': tipo_pessoa}

    def __init__(self, nome, nascimento, email, senha, telefone, endereco:Endereco):
        self.nome = nome
        self.nascimento = nascimento
        self.email = email
        self.senha = senha
        self.telefone = telefone
        self.endereco = endereco

    def __repr__(self):
        return '<Nome: {}\n Data de Nascimento: {}\n Email: {}\n Telefone: {}>'.format(self.nome, self.nascimento, self.email, self.telefone)
