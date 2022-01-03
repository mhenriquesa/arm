import requests
from os import getenv

token = getenv('ARM_WP_API')
url = "https://anaramosmoda.com.br/wp-json/wp/v2/posts"
headers = {'Authorization': token}
data = {
    "title": "post teste"
}

response = requests.post(url, json=data, headers=headers)
print(response)
