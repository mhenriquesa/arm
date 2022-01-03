from woocommerce import API
from os import getenv

ckey = getenv('ARM_WOO_CKEY')
csec = getenv('ARM_WOO_CSEC')

wcapi = API(
    url="https://anaramosmoda.com.br",
    consumer_key=ckey,
    consumer_secret=csec,
    wp_api=True,
    version="wc/v3"
)


def get_orders():
    r = wcapi.get("orders").json


def create_product(data):
    data = {
        "name": data.name,
        "type": "simple",
        "regular_price": data.regularprice,
        "description": data.desc,
        "categories": data.categories,
        "images": data.images
    }
    print(wcapi.post("products", data).json())
