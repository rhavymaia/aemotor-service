from helpers.database import db
from flask_restful import fields

rota_fields = {
    'id': fields.Integer(attribute='id'),
    'nomeDestino': fields.String(attribute='nomeDestino'),
    'qtdalunos': fields.String(attribute='qtdalunos'),
    'prefeitura': fields.String(attribute='prefeitura'),
    'veiculo': fields.String(attribute='veiculo'),
    'passageiro': fields.String(attribute='passageiro'),
    'horaSaida': fields.String(attribute='horaSaida'),
    'horaChegada': fields.String(attribute='horaChegada')
}

class Rota(db.Model):
    
    
    __tablename__ = 'tb_Rota'

    id = db.Column(db.Integer, primary_key=True)
    nomeDestino = db.Column(db.String(30), nullable=True)
    qtdalunos = db.Column(db.String(11), nullable=True)
    prefeitura = db.Column(db.String(80), nullable=True)
    veiculo = db.Column(db.String(30), nullable=True)
    passageiro = db.Column(db.String(11), nullable=True)
    horaSaida = db.Column(db.String(80), nullable=True)
    horaChegada = db.Column(db.String(80), nullable=True)
  
   
    def __init__(self, nomeDestino, qtdalunos, prefeitura, veiculo, passageiro, horaSaida, horaChegada):
        self.nomeDestino = nomeDestino
        self.qtdalunos = qtdalunos
        self.prefeitura = prefeitura        
        self.veiculo = veiculo
        self.passageiro = passageiro
        self.horaSaida = horaSaida
        self.horaChegada = horaChegada

    def __repr__(self):
        return 'Nome destino {}  Quantidade de Alunos {} Prefeitura {} Veiculo {} Passageiro {} Hora de Saída {} Hora de chegada {}\n'.format(self.nomeDestino, self.qtdalunos, self.prefeitura, self.veiculo, self.passageiro, self.horaSaida, self.horaChegada)