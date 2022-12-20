from helpers.database import db
from flask_restful import fields

convite_fields = {
    'id': fields.Integer(attribute='id'),
    'email': fields.String(attribute='email'),
    'mensagem': fields.String(attribute='mensagem'),
}
class Convites(db.Model):
    __tablename__ = "tb_convite"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80), nullable=False)
    mensagem = db.Column(db.String(500), nullable=False)

    
    def __init__(self, email, mensagem):
        self.email = email
        self.mensagem = mensagem


    def __repr__(self):
        return f'Convites(Email={self.email}, Mensagem={self.mensagem})'