from woocommerce import API

wcapi = API(
    url="https://anaramosmoda.com.br",
    consumer_key="ck_c507cb8d5bb8fb8c5024ccfea84fa9c74f1c37a5",
    consumer_secret="cs_be47a16de8fdf9fd613cc0567b252dcd38b6aa33",
    version="wc/v3"
)

r = wcapi.get("orders")
orders = r.json()

# orders é uma lista com os pedidos em dict

for order in orders:
    print(order['id'])
    print(order['billing']['first_name'])
