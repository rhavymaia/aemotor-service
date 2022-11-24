from model.pessoa import Pessoa
from helpers.database import db
class GestorApp(Pessoa,db.Model):
    
    __tablename__ = 'tb_gestorApp'
    __mapper_args__ = {'polymorphic_identity': 'gestor', 'concrete': True}
    
    id_gestor = db.Column(db.Integer, primary_key=True)
    gestorApp = db.Column(db.String(80), nullable=False)
    
    pessoa_id = db.Column(db.Integer, db.ForeignKey("tb_pessoa.id"))
    prefeitura_id = db.Column(db.Integer, db.ForeignKey('tb_prefeitura.id'), nullable=False)
   
    
    def __init__(self,pessoa):
        self.pessoa = pessoa

    def __repr__(self):
        return 'GestorApp {}\n'.format(self.pessoa)