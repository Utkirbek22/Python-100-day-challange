from calendar import month

import requests
from datetime import *

pixel_endpoint = "https://pixe.la/v1/users"
TOKEN = "adsdfsgfsdf"
USERNAME = "utkirbek"
GRAPH_ID = "graph1"

graph_endpoint = f"{pixel_endpoint}/{USERNAME}/graphs"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# respone = requests.post(url=pixel_endpoint,json=user_params)
# print(respone.text)

graph_config ={
    "id": GRAPH_ID,
    "name": "Graphical graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint,json=graph_config, headers=headers)
#
# print(response.text)

today = datetime(year=2026, month=4,day=29)

pixal_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "6.2"
}

pixel_creation_endpoint = f"{pixel_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

response1 = requests.post(url=pixel_creation_endpoint,json=pixal_data, headers=headers)
print(response1.text)