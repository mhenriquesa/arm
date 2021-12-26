from flask import Flask, request, Response


app = Flask(__name__)


@app.route('/')  # this is the home page route
def hello_world():  # this is the home page function that generates the page code
    return "Hello world!"


@app.route('/bot_webhook', methods=['POST'])
def botwebhook():
    req = request.get_json(silent=True, force=True)
    print(req)


@app.route('/mercadopago_webhook', methods=['POST'])
def mercadopagowebhook():
    req = request.get_json(silent=True, force=True)
    print(req)
    if req is not None:
        return Response(status=200)


if __name__ == '__main__':
    app.run(debug=True)
