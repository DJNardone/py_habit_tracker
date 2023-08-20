import requests
from datetime import datetime
import os

USERNAME = os.environ.get("USERNAME")
TOKEN = os.environ.get("TOKEN")
GRAPH_ID = "graph1"
headers = {
    "X-USER-TOKEN": TOKEN
}

#  CREATE USER PROFILE
pixela_endpoint = "https://pixe.la/v1/users"
parameters = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
# response = requests.post(url=pixela_endpoint, json=parameters)
# print(response.text)

# CREATE A PIXELA GRAPH
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": GRAPH_ID,
    "name": "Coding Graph",
    "unit": "minutes",
    "type": "int",
    "color": "sora"
}
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# POST DATA TO CREATE "PIXELS" ON THE GRAPH
today = datetime.now()
formatted_date = today.strftime("%Y%m%d")

post_pixel_endpoint = f"{graph_endpoint}/{GRAPH_ID}"
pixel_config = {
    "date": formatted_date,
    "quantity": input("How many minutes did you code today?"),
}
response = requests.post(url=post_pixel_endpoint, json=pixel_config, headers=headers)
print(response.text)

# UPDATE PIXEL DATA
# update_data_endpoint = f"{graph_endpoint}/{GRAPH_ID}/{formatted_date}"
# data_config = {
#     "quantity": "150"
# }
# response = requests.put(url=update_data_endpoint, json=data_config, headers=headers)
# print(response.text)

# DELETE PIXEL DATA
# response = requests.delete(url=update_data_endpoint, headers=headers)
# print(response.text)
