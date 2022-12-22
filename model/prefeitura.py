from helpers.database import db
class Prefeitura(db.Model):
    __tablename__ = "tb_prefeitura"

    id = db.Column(db.Integer, primary_key=True)
    nomePrefeito = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    secretarios=db.Column(db.String(120), nullable=False)
    telefone=db.Column(db.String(120), nullable=False)

    def __init__(self, secretarios, email, telefone, nomePrefeito):
        self.secretarios = secretarios
        self.email = email
        self.telefone = telefone
        self.nomePrefeito = nomePrefeito

    def __repr__(self):
        return 'Secretarios: {} Email: {} Telefone: {} Nome do Prefeito: {}\n'.format(self.secretarios, self.email, self.telefone, self.nomePrefeito)