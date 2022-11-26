from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from resources.endereco import Enderecos
#from resources.funcionario import Funcionario
from resources.login import Login

from helpers.database import db, migrate

#from model.endereco import Endereco
#from model.pessoa import Pessoa
#from model.aluno import Aluno

# CORS
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

# SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://marcella:409014@localhost:5432/aemotor-service"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate.init_app(app, db)

api = Api(app)


api.add_resource(Enderecos, '/enderecos')
#api.add_resource(Funcionario, '/funcionarios')
api.add_resource(Login, '/login')
if __name__ == '__main__':
    app.run(debug=False)
