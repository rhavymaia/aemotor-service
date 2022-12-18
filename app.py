from flask import Flask
from flask_restful import Api
from flask_cors import CORS

#Resources
from resources.cidade import Cidades
from resources.funcionario import Funcionarios
from resources.gestorApp import GestorApps  
from resources.index import IndexResource
from resources.instituicaoEnsino import InstituicaoDeEnsinos
from resources.endereco import Enderecos
from resources.rota import Rotas
from resources.pessoa import Pessoas
from resources.aluno import Alunos
from resources.prefeitura import Prefeituras
from resources.prefeito import Prefeitos
from resources.passageiro import Passageiros
from resources.motorista import Motoristas
from resources.uf import Ufs
from resources.veiculo import Veiculos

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
=======
api.add_resource(Enderecos, '/enderecos')

