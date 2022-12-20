from flask import Flask
from flask_restful import Api
from flask_cors import CORS

from helpers.database import db, migrate


from model.convite import Convites

from resources.convite import ConvitesResource
# CORS
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

# SQLAlchemy
# app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://pweb:123456@localhost:5432/aemotor"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:123456@localhost:5432/aemotor"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate.init_app(app, db)

api = Api(app)
convite = Convites("email@gmail.com", "Venha se cadastrar no nosso aplicativo")
print(convite)
api.add_resource(ConvitesResource, '/prefeitura/convite')



if __name__ == '__main__':
    app.run(debug=False)
