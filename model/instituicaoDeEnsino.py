from helpers.database import db
class InstituicaoDeEnsino(db.Model):
    
    __tablename__ = 'tb_InstituicaoDeEnsino'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(30), nullable=False)
    telefone = db.Column(db.String(11), nullable=False)
    logradouro = db.Column(db.String(80), nullable=False)
    aluno_id = db.Column(db.Integer, db.ForeignKey("tb_aluno.id"))
    rota_id = db.Column(db.Integer, db.ForeignKey('tb_Rota.id'), nullable=False)
    
    endereco = db.relationship("Endereco", uselist=False)
   
    def __init__(self, nome, logradouro, telefone):
        self.nome = nome
        self.logradouro = logradouro
        self.telefone = telefone

    def __repr__(self):
        return 'Nome: {} Logradouro: {} Telefone: {}\n'.format(self.nome, self.logradouro, self.telefone)