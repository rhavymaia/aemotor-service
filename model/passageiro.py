from helpers.database import db
from sqlalchemy import ForeignKey
from flask_restful import fields

passageiro_fields = {
    'id': fields.Integer(attribute='id'),
    'nome': fields.String(attribute='nome'),
    'cidadeOrigem': fields.String(attribute='cidadeOrigem'),
    'cidadeDestino': fields.String(attribute='cidadeDestino')

}

class Passageiro(db.Model):
    __tablename__ = 'tb_passageiro'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    cidadeOrigem = db.Column(ForeignKey("tb_cidade.id"), nullable=False)
    cidadeDestino = db.Column(ForeignKey("tb_cidade.id"), nullable=False)    
    
    
    
    def __init__(self, aluno, cidadeOrigem, cidadeDestino):
        self.aluno = aluno
        self.cidadeOrigem = cidadeOrigem
        self.cidadeDestino = cidadeDestino

    def __repr__(self):
        return 'Aluno {}\nCidade Origem {} Cidade Destino {}\n '.format(self.aluno, self.cidadeOrigem, self.cidadeDestino)