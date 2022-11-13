from helpers.database import db

class Login(db.Model):

    __tablename__ = 'login'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(200), unique=True, nullable=False)
    password = db.Column(db.String(500), unique=True, nullable=False)

    def __init__(self, nome, email, password):
        self.nome = nome
        self.email = email
        self.password = password

    def __repr__(self):
        return '<Nome: {}>'.format(self.nome)


