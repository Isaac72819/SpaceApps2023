import requests


query_params = {"gender": "female", "nat": "de"}
url = ("https://randomuser.me/api/",query_params)

response = requests.get(url)
response.json()
print(response.content)
