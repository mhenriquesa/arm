import mercadopago

sdk = mercadopago.SDK(
    "TEST-4019755699686949-122117-d66a5a2dea08328238ef6a022782e5c5-475891059")

# Cria um item na preferência
preference_data = {
    "items": [
        {
            "title": "My Item",
            "quantity": 1,
            "unit_price": 75.76
        }
    ]
}

preference_response = sdk.preference().create(preference_data)
preference = preference_response["response"]
