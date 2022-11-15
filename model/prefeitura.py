from helpers.database import db

class Prefeitura(db.Model):
    
    __tablename__ = "tb_prefeitura"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(120), unique=True, nullable=False)
    endereco=db.Column(db.String(120), nullable=False)
    nomePrefeito = db.Column(db.String(100), unique=True, nullable=False)
    
    def __init__(self, nome, endereco, nomePrefeito):
        self.nome = nome
        self.endereco = endereco
        self.nomePrefeito= nomePrefeito

    def __repr__(self):
        return '<Nome: {}, Endereco: {}, Nome do Prefeito: {}>'.format(self.nome, self.endereco, self.nomePrefeito)
