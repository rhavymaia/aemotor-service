from model.endereco import endereco_fields
from helpers.database import db
from sqlalchemy import ForeignKey
from flask_restful import fields

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

class Funcionario(db.Model):
    __tablename__ = "tb_funcionario"
    __mapper_args__ = {'polymorphic_identity': 'funcionario'}
    
    id_fun = db.Column(ForeignKey("tb_pessoa.id"), primary_key=True)
    prefeitura = db.Column(db.String(90), nullable=False)
    cargo = db.Column(db.String(30), nullable=False)
    
    prefeitura_id = db.Column(db.Integer, db.ForeignKey('tb_prefeitura.id'), nullable=False)
    
    motorista = db.relationship("Motorista", uselist=False)
    
    def __init__(self, nome, nascimento, email, telefone, endereco, prefeitura, cargo):
        super().__init__(nome, nascimento, email, telefone, endereco)
        self.prefeitura = prefeitura
        self.cargo = cargo

    def __repr__(self):
        return '\nPrefeitura {}\n Cargo {}\n'.format(self.prefeitura, self.cargo)

    