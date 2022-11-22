from flask import Flask
from flask_restful import Api
from flask_cors import CORS

#Model

from model.endereco import Endereco_db
from model.pessoa import Pessoa_db
from model.aluno import Aluno_db
from model.funcionario import Funcionario_db
from model.gestorApp import GestorApp_db
from model.instituicaoDeEnsino import InstituicaoDeEnsino_db
from model.motorista import Motorista_db
from model.passageiro import Passageiro_db
from model.pessoa import Pessoa_db
from model.prefeito import Prefeito_db
from model.prefeitura import Prefeitura_db
from model.rota import Rota_db
from model.cidade import Cidade_db
from model.uf import Uf_db
from model.veiculo import Veiculo_db

#Resources

from resources.cidade import Cidade
from resources.funcionario import Funcionario
from resources.gestorApp import GestorApp  
from resources.index import IndexResource
from resources.instituicaoEnsino import InstituicaoDeEnsino
from resources.endereco import Endereco
from resources.rota import Rota
from resources.pessoa import Pessoa
from resources.aluno import Aluno
from resources.prefeitura import Prefeitura
from resources.prefeito import Prefeito
from resources.passageiro import Passageiro
from resources.motorista import Motorista
from resources.uf import Uf
from resources.veiculo import Veiculo

from helpers.database import db, migrate

# CORS
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

# SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://service:juvenal@localhost:5432/aemotor'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate.init_app(app, db)


api = Api(app)

api.add_resource(IndexResource, '/')
api.add_resource(Endereco, '/enderecos')
api.add_resource(Pessoa, '/pessoas')
api.add_resource(Prefeitura, '/prefeituras')
api.add_resource(Aluno, '/alunos')
api.add_resource(InstituicaoDeEnsino, '/instituicoes')
api.add_resource(Funcionario, '/funcionarios')
api.add_resource(GestorApp, '/gestorApps')
api.add_resource(Cidade, '/cidades')
api.add_resource(Motorista, '/motoristas')
api.add_resource(Passageiro, '/passageiros')
api.add_resource(Rota, '/rotas')
api.add_resource(Prefeito, '/prefeitos')
api.add_resource(Uf, '/ufs')
api.add_resource(Veiculo, '/veiculos')

