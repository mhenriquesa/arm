from flask import request, Response, Blueprint
from webhookserver.melhorenvioapi import calcular_frete
from webhookserver.models import Client, Cart, Products

main = Blueprint('main', __name__)


@main.route('/')
def hello_world():
    prod = Products('c13', 'Calça', 'Jeans', 'Modeladora',
                    139, 'P M G GG', 'http', 'https', 1)

    Products.create_prod(prod)
    return "Hello world!"


@main.route('/bot_webhook', methods=['POST'])
def botwebhook():
    data = request.get_json(silent=True, force=True)
    action = data['queryResult']['action']
    intent = data['queryResult']['intent']['displayName']
    categorie = data['queryResult']['parameters']['itemescolhido']

    if action == 'querverfoto':

        produtos = Products.get_categorie(categorie)
        print(produtos)

    if action == "ver_carrinho":
        client_phone = int(data['queryResult']['parameters']['telefone'])
        clientid = Client.find_by_phone(client_phone)

        cart = Cart.get_cart(clientid[0].id)
        return cart

    if action == "consultar_frete":
        return calcular_frete(data)

    return Response(status=200)


@main.route('/mercadopago_webhook', methods=['POST'])
def mercadopagowebhook():
    data = request.get_json(silent=True, force=True)
    print(data)
    if data is not None:
        return Response(status=200)
