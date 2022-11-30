from flask import Flask
from flask_restful import Api
from flask_cors import CORS

#Model

from model.endereco import Endereco
from model.pessoa import Pessoa
from model.aluno import Aluno
from model.funcionario import Funcionario
from model.gestorApp import GestorApp
from model.instituicaoDeEnsino import InstituicaoDeEnsino
from model.motorista import Motorista
from model.passageiro import Passageiro
from model.prefeito import Prefeito
from model.prefeitura import Prefeitura
from model.rota import Rota
from model.cidade import Cidade
from model.uf import Uf
from model.veiculo import Veiculo

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
api.add_resource(Enderecos, '/enderecos')
api.add_resource(Pessoas, '/pessoas')
api.add_resource(Prefeituras, '/prefeituras')

api.add_resource(Alunos, '/alunos')
# api.add_resource(Alunos, '/alunos/<int:id>')

api.add_resource(InstituicaoDeEnsinos, '/instituicoes')
api.add_resource(Funcionarios, '/funcionarios')
api.add_resource(GestorApps, '/gestorApps')
api.add_resource(Cidades, '/cidades')
api.add_resource(Motoristas, '/motoristas')
api.add_resource(Passageiros, '/passageiros')
api.add_resource(Rotas, '/rotas')
api.add_resource(Prefeitos, '/prefeitos')
api.add_resource(Ufs, '/ufs')
api.add_resource(Veiculos, '/veiculos')

