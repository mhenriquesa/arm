import requests
from os import getenv
import json

token = getenv('ARM_WP_API')
url = "https://anaramosmoda.com.br/wp-json/wp/v2/media"
headers = {'Authorization': token}
data = {
    "file": open('d:\Programming\Projetos\\armbot\webhookserver\image.jpg', 'rb')
}

response = requests.post(url, files=data, headers=headers)
# response = requests.post(url, json=data, headers=headers)
imgurl = str(json.loads(response.content)['source_url'])
print(imgurl)
