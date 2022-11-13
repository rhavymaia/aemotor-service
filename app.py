from flask import Flask, session, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from flask_cors import CORS

from werkzeug.security import check_password_hash
import psycopg2
import psycopg2.extras

from helpers.database import db, migrate
from resources.endereco import Endereco

from model.endereco import Endereco

from model.login import Login


# CORS
app = Flask(__name__)
app.config['SECRET_KEY'] = 'cairocoders-ednalan'

CORS(app, resources={r"/*": {"origins": "*"}})


# SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://marcella:409014@localhost:5432/aemotor-service"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

DB_HOST = "localhost"
DB_NAME = "aemotor-service"
DB_USER = "marcella"
DB_PASS = "409014"
     
conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)


@app.route('/')
def home():
    if 'email' in session:
        email = session['email']
        resp = jsonify({'MENSAGEM' : 'Você já está logado!'})
        resp.status_code = 200
        return resp
    else:
        resp = jsonify({'MENSAGEM' : 'Não autorizado.'})
        resp.status_code = 401
        return resp

@app.route('/login', methods=['POST'])
def login():
    _json = request.json
    _email = _json['email']
    _password = _json['password']
    #print(_password)
    #valida os valores recebidos
    if _email and _password:
        #checa se o usuário existe  
        cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
          
        sql = "SELECT * FROM login WHERE email=%s" #query
        sql_where = (_email,) #busca

        cursor.execute(sql, sql_where)
        #row pega tudo da linha correspondente indicada
        row = cursor.fetchone()
        email = row['email']
        password = row['password']

        if row:

            if check_password_hash(password, _password):
                session['email'] = email
                cursor.close()
                resp = jsonify({'MENSAGEM' : 'Você logou com sucesso!'})
                resp.status_code = 200
                return resp
            else:
                resp = jsonify({'MENSAGEM' : 'Senha inválida.'})
                resp.status_code = 400
                return resp

    else:
        resp = jsonify({'MENSAGEM' : 'Credenciais inválidas.'})
        resp.status_code = 400
        return resp


@app.route('/logout')
def logout():
    if 'email' in session:
        session.pop('email', None)
    return jsonify({'MENSAGEM' : 'Você saiu com sucesso!'})
          

db.init_app(app)
migrate.init_app(app, db)

with app.app_context():
    db.create_all()

db = SQLAlchemy(app)
api = Api(app)

#api.add_resource(Endereco, '/enderecos')


if __name__ == '__main__':
    app.run(debug=False)

