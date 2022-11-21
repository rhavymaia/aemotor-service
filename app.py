from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from model.funcionario import Funcionario
from model.aluno import Aluno

from resources.endereco import Enderecos
from resources.funcionario import Funcionarios
from resources.cadastroEstudante import cadastroEstudantes

from helpers.database import db, migrate

# CORS
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

# SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://hacjesse:hacjesse@localhost:5432/aemotor"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate.init_app(app, db)

api = Api(app)

api.add_resource(Enderecos, '/enderecos')
api.add_resource(Funcionarios, '/funcionarios')
api.add_resource(cadastroEstudantes, '/cadastroEstudantes')

if __name__ == '__main__':
    app.run(debug=False)
