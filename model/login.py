from helpers.database import db
from model.pessoa import Pessoa, pessoa_fields
from flask_restful import fields

login_fields = {
    'id': fields.Integer(attribute='id'),
    'pessoa': fields.Nested(pessoa_fields),
    'data_login': fields.String(attribute='data_login'),
    'key': fields.String(attribute='key')
}


class Login(Pessoa, db.Model):

    __tablename__ = 'tb_login'

    id = db.Column(db.Integer, primary_key=True)

    pessoa_id = db.Column(db.Integer, db.ForeignKey("tb_pessoa.id"))

    datahora = db.Column(db.DateTime)

    key = db.Column(db.String(40), unique=True)

    # Relacionamento com Pessoa
    pessoa = db.relationship("Pessoa", uselist=False, passive_updates=False)

    def __init__(self, pessoa, datahora, key):
        self.pessoa = pessoa
        self.datahora = datahora
        self.key = key

    def __repr__(self):
        return '<Login pessoa: {}\n data: {}>'.format(self.pessoa, self.datahora)
