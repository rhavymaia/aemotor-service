from helpers.database import db
from sqlalchemy import ForeignKey

class Motorista(db.Model):
    __tablename__ = 'tb_motorista'
    __mapper_args__ = {'polymorphic_identity': 'Motorista'}
    
    id = db.Column(ForeignKey("tb_pessoa.id"), primary_key=True)
    rotas = db.Column(db.String(80), nullable=False)
    
    
    veiculo = db.relationship('Veiculo',uselist=False)
    
    def __init__(self, rotas,funcionario):
        self.funcionario = funcionario
        self.rotas = rotas

    def __repr__(self):
        return 'Rotas {}\n '.format(self.rotas, self.funcionario)