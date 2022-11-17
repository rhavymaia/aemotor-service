from model.pessoa import Pessoa
from helpers.database import db
from flask_restful import fields

from model.endereco import endereco_fields

funcionario_fields = {
    'id': fields.Integer(attribute='id'),
    'nome': fields.String(attribute='nome'),
    'nascimento': fields.String(attribute='nascimento'),
    'email': fields.String(attribute='email'),
    'telefone': fields.String(attribute='telefone'),
    'prefeitura': fields.String(attribute='prefeitura'),
    'cargo': fields.String(attribute='cargo'),
    'endereco': fields.Nested(endereco_fields)
}


class Funcionario(Pessoa, db.Model):

    __tablename__ = "tb_funcionario"
    __mapper_args__ = {'polymorphic_identity': 'funcionario', 'concrete': True}

    id = db.Column(db.Integer, primary_key=True)
    prefeitura = db.Column(db.String, nullable=False)
    cargo = db.Column(db.String, nullable=False)

    nome = db.Column(db.String, unique=True, nullable=False)
    nascimento = db.Column(db.Date)
    email = db.Column(db.String, unique=True)
    telefone = db.Column(db.String(11))
    endereco = db.relationship("Endereco", uselist=False)

    def __init__(self, nome, nascimento, email, telefone, endereco, prefeitura, cargo):
        super().__init__(nome, nascimento, email, telefone, endereco)
        self.prefeitura = prefeitura
        self.cargo = cargo

    def __repr__(self):
        return '<Funcionario - Nome: {}\n>'.format(self.nome)
