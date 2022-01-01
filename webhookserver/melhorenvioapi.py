import json
import requests
from os import getenv

menviourl = "https://www.melhorenvio.com.br/api/v2/me/shipment/calculate"
menviotoken = menvio = getenv('ARM_MENVIO')


def calcular_frete(req):

    cepdestino = req['queryResult']['parameters']['cep']
    payload = json.dumps({
        "from": {
            "postal_code": "09172180"
        },
        "to": {
            "postal_code": cepdestino
        },
        "products": [
            {
                "id": "x",
                "width": 11,
                "height": 17,
                "length": 11,
                "weight": 1,
                "insurance_value": 0,
                "quantity": 1
            }
        ]
    })
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': menviotoken,
        'User-Agent': 'armbot henriqueator@gmail.com'
    }

    response = requests.request(
        "POST", menviourl, headers=headers, data=payload)

    data = response.json()

    if 'error' in data[1]:
        valorsedex = "Não disponível"
    else:
        valorsedex = data[1]['price']

    if 'error' in data[0]:
        valorpac = 'Não disponível'
    else:
        valorpac = data[0]['price']

    return {
        "fulfillmentText": f''' 
          O frete de São Paulo para o cep {cepdestino}  fica:
          SEDEX: {valorsedex} 
          PAC: {valorpac}''',
        "source": 'webhook'
    }
