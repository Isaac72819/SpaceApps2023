from bs4 import BeautifulSoup
from urllib.request import urlopen

url = "https://data.noaa.gov/onestop/collections?q=climate"
page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")

for link in soup.find_all("a"):
    link_url = url + link["href"]
    print(link_url)