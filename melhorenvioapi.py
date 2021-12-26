from flask import request
import requests
import json

menviourl = "https://www.melhorenvio.com.br/api/v2/me/shipment/calculate"


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
        'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6ImUyMzc5NDM4YmJhY2Q4NzA2NWE1MTg0MjY3ZGY4YWYyZDgwOTY3ZDBjMmQ2ODc1MDg0ODNhODkyZGY1NzIxZDYwMGJiMWY5MDVhNmM2ODdmIn0.eyJhdWQiOiIxIiwianRpIjoiZTIzNzk0MzhiYmFjZDg3MDY1YTUxODQyNjdkZjhhZjJkODA5NjdkMGMyZDY4NzUwODQ4M2E4OTJkZjU3MjFkNjAwYmIxZjkwNWE2YzY4N2YiLCJpYXQiOjE2Mzk4ODI4NzQsIm5iZiI6MTYzOTg4Mjg3NCwiZXhwIjoxNjcxNDE4ODc0LCJzdWIiOiJkODBkZGZhZi1jMTEwLTRmM2UtYmU0MS0yNDM0YTgxMmU5ZGYiLCJzY29wZXMiOlsic2hpcHBpbmctY2FsY3VsYXRlIiwic2hpcHBpbmctdHJhY2tpbmciXX0.u_3vTKRVsUgBSVtc5x8PO75S-hZbHARTsKtdP79QupVqjF74XD9Mr7WHtDQSqP60YA6YRw8VHa6i3Fkp9BZdxbKyT0NdVRZCjK3yVk6IKJtSODpMfp5x1BmiIiT0o5JfA9JkxlFmfGpJmwH_VFo12X9HAbyVqNqa2z07xtsMXc7t5-MrB8e6Wh2Zmu0tiYPf5xPerNqIqWsZ1oMU9GLbKjdjQh2k8OB6LfhYNs2a2KOdbgjfRXeqnq1qSV9VQDkJHUQ4fGmdolXyq-9sixBuvxgSFpdAhCjKkjx1mE9gahosOsxN4OF7mi8GhBiqghyJ5wQaiW-3Q0ZXRFCtAc9RZV6Pao6eBxjIgrv4iPcgUr71lgUVdIYkFl28YlFbZvHIz0xs6tdNL_b8lipmZYxdlr7fsa-434JKJi0XATrsqwyE1xJ3NxK1MqSkDJH2mzdtBLe3RsrNp2R7AwHyWbphZ1-ukVq6Cl9JPv7jZ4__OiTrVgC65u8bvz3h0lRcN1pwM25RK9pLYVJnxzVZ-CHY6g0FihPQaCzEz4rF8uN22JZTukaog--e6z1CGuRX4oUTspjrVPeZv6bt2j241iq9TbT1mZoiKO-A3KVAz1R1JpeRS8nr6jQEDgbqFXAh1R0znecA7dcPVhrk_yEylkIXYvX90IiDN39m9d_06ricSJ4',
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

    #print(data[0]['company']['name'], data[1])
    #fretesedex = data[0]['company']['name'], data[0]
    return {
        "fulfillmentText": f''' 
          O frete de São Paulo para o cep {cepdestino}  fica:
          SEDEX: {valorsedex} 
          PAC: {valorpac}''',
        "source": 'webhook'
    }
