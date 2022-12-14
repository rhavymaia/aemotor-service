
import smtplib
from flask_restful import (Resource, current_app, marshal, marshal_with,
                           reqparse)
from sqlalchemy import exc
import email.message
from helpers.database import db
from model.convites import Convites, convite_fields
from model.error import Error, error_campos

parser = reqparse.RequestParser()
parser.add_argument('email', required=True)
parser.add_argument('mensagem', required=True)

class ConvitesResource(Resource):
    @marshal_with(convite_fields)
    def get(self):
        current_app.logger.info("Get - Convites")
        convites = Convites.query.all()
        return convites, 200

    def post(self):
        current_app.logger.info("Post - Convites")
        try:
            # JSON
            args = parser.parse_args()
            emails = args['email']
            mensagem = args['mensagem']

            corpo_email = "<p>"+emails+"</p>"+"<p>"+mensagem+"</p>"
            
            msg = email.message.Message()
            msg['Subject'] = "Aê Motô - Gerenciador de transporte escolar"
            msg['From']  = "alessandraavelino21@gmail.com"
            msg['To'] = emails
            password = "fqtlqfuzdoldjzpv" #Essa senha será gerada através de uma config lá do google
            msg.add_header("Content-Type", "text/html")
            msg.set_payload(corpo_email)

            s = smtplib.SMTP('smtp.gmail.com: 587')
            s.starttls()
            s.login(msg['From'], password)
            s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
            print("Email enviado com sucesso!!")

            convite = Convites(emails, mensagem)

            db.session.add(convite)
            db.session.commit()
        except exc.SQLAlchemyError as err:
            current_app.logger.error(err)
            erro = Error(1, "Erro ao adicionar no banco de dados, consulte o adminstrador",
                         err.__cause__())
            return marshal(erro, error_campos), 500

        return 204

    
