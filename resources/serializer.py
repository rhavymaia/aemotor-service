from model.endereco import Endereco
from model.prefeitura import Prefeitura

def response_serializer(enderecos: Endereco):
    response = []
    for endereco in enderecos:
        endereco_dict = {
            "nome": endereco.cep,
            "numero": endereco.numero,
            "complemento": endereco.complemento,
            "referencia": endereco.referencia,
            "logradouro": endereco.logradouro
        }
        response.append(endereco_dict)
    return response

def response_serializer_prefeitura(prefeituras: Prefeitura):
    response = []
    for prefeitura in prefeituras:
        prefeitura_dict = {
            "nome": prefeitura.nome,
            "endereco": prefeitura.endereco,
            "nomePrefeito": prefeitura.nomePrefeito,
        }
        response.append(prefeitura_dict)
    return response