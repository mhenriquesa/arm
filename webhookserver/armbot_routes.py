from flask import request, Response, Blueprint
import webhookserver.armbot_db_functions
from webhookserver.models import Client
from webhookserver import db


main = Blueprint('main', __name__)


@main.route('/')  # this is the home page route
def hello_world():  # this is the home page function that generates the page code
    user1 = Client(username="Filho", email="zzzzz", phone="1111")
    db.session.add(user1)
    db.session.commit()
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
