#from sqlalchemy import ForeignKey
from helpers.database import db

from flask_restful import fields

login_fields = {
'id': fields.Integer(attribute='id'),
'email': fields.String(attribute='email'),
'senha': fields.String(attribute='senha')
}


class Login(db.Model):

    __tablename__ = 'tb_login'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(200), unique=True, nullable=False)
    senha = db.Column(db.String(100), nullable=False)

    #pessoa_id = db.Column(db.Integer, db.ForeignKey("tb_pessoa.id"))

    def __init__(self, email, senha):
        # super().__init__(nome, nascimento, email, senha, telefone, endereco)
        self.email = email
        self.senha = senha
