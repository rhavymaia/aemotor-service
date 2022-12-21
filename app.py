from flask import Flask
from flask_restful import Api
from flask_cors import CORS

from resources.endereco import Enderecos
from resources.funcionario import FuncionariosResource, FuncionarioResource


from helpers.database import db, migrate

# CORS
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

# SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:1234@localhost:5432/postgres"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate.init_app(app, db)

api = Api(app)


api.add_resource(Enderecos, '/enderecos')
api.add_resource(FuncionariosResource, '/funcionarios')
api.add_resource(FuncionarioResource, '/funcionarios/<int:id>')


if __name__ == '__main__':
    app.run(debug=False)