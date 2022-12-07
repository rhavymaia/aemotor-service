from helpers.database import db
from sqlalchemy import ForeignKey
from flask_restful import fields

from model.cidade import cidade_fields

passageiro_fields = {
    'id': fields.Integer(attribute='id'),
    'nome': fields.String(attribute='nome'),
    'cidadeOrigem': fields.Nested(cidade_fields),
    'cidadeDestino': fields.Nested(cidade_fields)
}


class Passageiro(db.Model):
    __tablename__ = 'tb_passageiro'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)

    cidadeorigem_id = db.Column(db.Integer, db.ForeignKey("tb_cidade.id"))
    cidadeOrigem = db.relationship("Cidade", uselist=False)

    cidadedestino_id = db.Column(db.Integer, db.ForeignKey("tb_cidade.id"))
    cidadeDestino = db.relationship("Cidade", uselist=False)

    def __init__(self, aluno, cidadeOrigem, cidadeDestino):
        self.aluno = aluno
        self.cidadeOrigem = cidadeOrigem
        self.cidadeDestino = cidadeDestino

    def __repr__(self):
        return 'Aluno {}\nCidade Origem {} Cidade Destino {}\n '.format(self.aluno, self.cidadeOrigem, self.cidadeDestino)
