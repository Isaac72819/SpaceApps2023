import requests
import json

url = "https://quickstats.nass.usda.gov/api/api_GET/?key=1394EAFD-B072-3B68-90F7-8F44F8625D1E&commodity_desc=CORN&year__GE=2012&state_alpha=VA&format=JSON"

response = requests.get(url)

#formattedData = json.dumps(response.json(), indent = 2)
#print(formattedData)

data = response.json()["data"]

print(f"Found {len(data)} Datas")

year = data[1]["year"]

#year = data.get("year", "Year Not Found")

print("Year:",year)