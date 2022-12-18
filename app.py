from flask import Flask
from flask_restful import Api
from flask_cors import CORS



from resources.aprovar import AprovadoResource
from helpers.database import db, migrate

from model.aprovar import Aprovacao


# CORS
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

# SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://pweb:123456@localhost:5432/aemotor'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate.init_app(app, db)

api = Api(app)





api.add_resource(AprovadoResource,'/convites/aprovado')


if __name__ == '__main__':
    app.run(debug=False)
