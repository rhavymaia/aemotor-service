from flask import Flask
from flask_restful import Api
from flask_cors import CORS

from resources.endereco import Enderecos
from resources.funcionario import Funcionarios,Funcionarios_Put
from helpers.database import db, migrate

from model.convite import Convites

from resources.convite import ConvitesResource

from model.endereco import Endereco
from model.pessoa import Pessoa
from model.aluno import Aluno

# CORS
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

# SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://service:juvenal@localhost:5432/aemotor'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate.init_app(app, db)

api = Api(app)
convite = Convites("email@gmail.com", "Venha se cadastrar no nosso aplicativo")
print(convite)
api.add_resource(ConvitesResource, '/prefeitura/convite')

api.add_resource(Enderecos, '/enderecos')
api.add_resource(Funcionarios, '/funcionarios')
api.add_resource(Funcionarios_Put, '/funcionarios/<int:id>')

if __name__ == '__main__':
    app.run(debug=False)
