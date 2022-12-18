from sqlalchemy import ForeignKey
from helpers.database import db
from model.pessoa import Pessoa
from flask_restful import fields

login_fields = {
    'id': fields.Integer(attribute='id'),
    'email': fields.String(attribute='email'),
    'senha': fields.String(attribute='senha')
}

class Login(Pessoa, db.Model):

    __tablename__ = 'tb_login'

    id = db.Column(db.Integer, primary_key=True)

    pessoa_id = db.Column(db.Integer, db.ForeignKey("tb_pessoa.id"))

    def __init__(self, nome, nascimento, email, senha, telefone, endereco):
        super().__init__(nome, nascimento, email, senha, telefone, endereco)