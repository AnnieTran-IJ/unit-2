
import requests
from datetime import datetime

from Tools.scripts.highlight import default_html

ip = "192.168.4.137"
request = requests.get(f"http://{ip}/readings")

user = {"username": "A_square", "password": "Ann&Annie"}
r = requests.post(f"http://{ip}/register", json = user)

answer = requests.post(f'http://{ip}/login', json=user)
cookie = answer.json()["access_token"]
print(cookie)

auth = {"Authorization": f"Bearer {cookie}"}

dht_t = {"type": "Temperature",
        "location": "Annie's Room",
        "name": "dht_asquare_1",
        "unit": "C"} #id: 185
r = requests.post(f'http://{ip}/sensor/new', json=dht_t, headers=auth)

dht_h = {"type": "Humidity",
        "location": "Annie's Room",
        "name": "dht_asquare_2",
        "unit": "%"} #id: 186

r = requests.post(f'http://{ip}/sensor/new', json=dht_h, headers=auth)
bme_t = {"type": "Temperature",
        "location": "Annie's Room",
        "name": "bme_asquare_1",
        "unit": "C"} #id: 187

r = requests.post(f'http://{ip}/sensor/new', json=bme_t, headers=auth)
bme_h = {"type": "Humidity",
        "location": "Annie's Room",
        "name": "bme_asquare_2",
        "unit": "%"} #id: 188

r = requests.post(f'http://{ip}/sensor/new', json=bme_h, headers=auth)

bme_p = {"type": "Pressure",
        "location": "Annie's Room",
        "name": "bme_asquare_3",
        "unit": "hPa"} #id:197
r = requests.post(f'http://{ip}/sensor/new', json=bme_p, headers=auth)

