from datetime import datetime
from sqlalchemy import ForeignKey
from helpers.database import db
from model.pessoa import Pessoa, pessoa_fields
from flask_restful import fields

login_campos = {
    'id': fields.Integer(attribute='id'),
    'pessoa': fields.Nested(pessoa_fields),
    'datahora': fields.String(attribute='data_login'),
    'key': fields.String(attribute='key')
}

class Login(Pessoa, db.Model):

    __tablename__ = 'tb_login'

    id = db.Column(db.Integer, primary_key=True)

    pessoa_id = db.Column(db.Integer, db.ForeignKey("tb_pessoa.id"))

    datahora = db.Column(db.DateTime, default=datetime.now)

    key = db.Column(db.String(40))

    pessoa = db.relationship("Pessoa", uselist=False)


    def __init__(self, pessoa: Pessoa, datahora, key):
        self.datahora = datahora
        self.pessoa = pessoa
        self.key = key

    def __repr__(self):
        return '<Login data: {}>'.format(self.datahora)
