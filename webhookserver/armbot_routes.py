from flask import request, Response, Blueprint
from sqlalchemy.orm import session
import webhookserver.armbot_db_functions
from webhookserver.models import Client, Cart, Products
from webhookserver import db
import json

main = Blueprint('main', __name__)

# def products_in_cart_by_id(clientid, )


@main.route('/')  # this is the home page route
def hello_world():  # this is the home page function that generates the page code

    # Cart.add(2, "L10", 5)
    Cart.remove(2, "L10", 1)

    return "Hello world!"


@main.route('/bot_webhook', methods=['POST'])
def botwebhook():
    req = request.get_json(silent=True, force=True)
    action = req['queryResult']['action']
    user_phone = int(req['queryResult']['parameters']['telefone'])

    if action == "ver_carrinho":
        webhookserver.armbot_db_functions.get_client_by_phone(user_phone)

    return Response(status=200)


@main.route('/mercadopago_webhook', methods=['POST'])
def mercadopagowebhook():
    req = request.get_json(silent=True, force=True)
    print(req)
    if req is not None:
        return Response(status=200)
