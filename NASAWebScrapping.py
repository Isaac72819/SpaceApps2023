import mechanicalsoup
from bs4 import BeautifulSoup
from urllib.request import urlopen

#Browser objects represent the headless web browser
browser = mechanicalsoup.Browser()

#You can use them to request a page from the Internet by passing a URL to their .get() method:
url = "https://data.noaa.gov/onestop/collections?q=climate"

page = browser.get(url)
page.soup

links = page.soup.select("a")

for link in links:
    address = link["href"]
    text = link.text
    print(f"{text} : {address}")
