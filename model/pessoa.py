from helpers.database import db
from sqlalchemy.types import String


class Pessoa(db.Model):

    __tablename__ = "tb_pessoa"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String, nullable=False)
    nascimento = db.Column(db.String(10), nullable=False)
    email = db.Column(db.String(200), nullable=False, unique=True)
    senha = db.Column(db.String(300), nullable=False)
    telefone = db.Column(db.String(11), nullable=False, unique=True)

    # Relacionamento com Endereco e Aluno
    endereco = db.relationship("Endereco", uselist=False)
    aluno_child = db.relationship("Aluno", uselist=False)
    # Herança: Superclasse
    tipo_pessoa = db.Column('tipo_pessoa', String(50))
    __mapper_args__ = {'polymorphic_on': tipo_pessoa}

    def __init__(self, nome, nascimento, email, senha, telefone, endereco):
        self.nome = nome
        self.nascimento = nascimento
        self.email = email
        self.senha = senha
        self.telefone = telefone
        self.endereco = endereco

    def __repr__(self):
        return '<Nome: {}\n Data de Nascimento: {}\n Email: {}\n Telefone: {}>'.format(self.nome, self.nascimento, self.email, self.telefone)
