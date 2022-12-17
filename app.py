from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from model.pessoa import Pessoa
from model.aluno import Aluno
from model.endereco import Endereco
from model.funcionario import Funcionario
from model.cidade import Cidade
from model.uf import Uf


from resources.endereco import Enderecos
from resources.funcionario import FuncionarioResource,FuncionariosResource
from helpers.database import db, migrate
from resources.aluno import AlunoResource,AlunosResource





# CORS
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

# SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://service:juvenal@localhost:5432/aemotor'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate.init_app(app, db)

api = Api(app)

api.add_resource(Enderecos, '/enderecos')
api.add_resource(FuncionariosResource, '/funcionarios')
api.add_resource(FuncionarioResource, '/funcionarios/<int:id>')
api.add_resource(AlunosResource, '/Alunos')
api.add_resource(AlunoResource, '/Aluno/<int:id>')


if __name__ == '__main__':
    app.run(debug=False)