import requests
from datetime import datetime


ip = "192.168.4.137"
request = requests.get(f"http://{ip}/readings")

user = {"username": "A_square", "password": "Ann&Annie"}
r = requests.post(f"http://{ip}/register", json = user)

answer = requests.post(f'http://{ip}/login', json=user)
cookie = answer.json()["access_token"]
print(cookie)

auth = {"Authorization": f"Bearer {cookie}"}

s1_t = {"type": "Temperature",
        "location": "Annie's Room",
        "name": "sensor_asquare_1",
        "unit": "C"
} #"owner_id": 52

r = requests.post(f'http://{ip}/sensor/new', json=s1_t, headers=auth)


