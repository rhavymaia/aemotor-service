from model.funcionario import Funcionario
from helpers.database import db

class Motorista(Funcionario,db.Model):
    __tablename__ = 'tb_motorista'
    __mapper_args__ = {'polymorphic_identity': 'motorista'}
    
    id = db.Column(db.Integer, primary_key=True)
    rotas = db.Column(db.String(80), nullable=False)
    
    
    veiculo = db.relationship('Veiculo',uselist=False)
    
    def __init__(self, rotas,funcionario):
        self.funcionario = funcionario
        self.rotas = rotas

    def __repr__(self):
        return 'Rotas {}\n '.format(self.rotas, self.funcionario)