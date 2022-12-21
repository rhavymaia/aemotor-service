
from helpers.database import db
class GestorApp(db.Model):
    
    __tablename__ = 'tb_gestorApp'
    
    id_gestor = db.Column(db.Integer, primary_key=True)
    gestorApp = db.Column(db.String(80), nullable=False)
    
    
    def __init__(self,pessoa):
        self.pessoa = pessoa

    def __repr__(self):
        return 'GestorApp {}\n'.format(self.pessoa)