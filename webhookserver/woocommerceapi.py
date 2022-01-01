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

r = wcapi.get("orders")
orders = r.json()
