from model.convites import Convites
from model.endereco import Endereco
def response_serializer(convites: Convites):
    response = []
    for convite in convites:
        convite_dict = {
            "email": convite.email,
            "mensagem": convite.mensagem
        }

        response.append(convite_dict)
    return response

def response_serializer_end(enderecos: Endereco):
    response = []
    for endereco in enderecos:
        endereco_dict = {
            "cep": endereco.cep,
            "numero": endereco.numero,
            "complemento": endereco.complemento,
            "referencia": endereco.referencia,
            "logradouro": endereco.logradouro,
        }
        response.append(endereco_dict)
    return response