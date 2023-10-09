# beauty_soup.py

from bs4 import BeautifulSoup
from urllib.request import urlopen

'''
url = "http://olympus.realpython.org/profiles/dionysus"
page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")
#The BeautifulSoup object assigned to soup is created with two arguments. 
# The first argument is the HTML to be parsed, and the second argument, the 
# string "html.parser", tells the object which parser to use behind the scenes. 
# "html.parser" represents Python’s built-in HTML parser.

print(soup.get_text())
#For example, BeautifulSoup objects have a .get_text() method that you can use 
# to extract all the text from the document and automatically remove any HTML tags.

image1, image2 = soup.find_all("img")
#return [<img src="/static/dionysus.jpg"/>, <img src="/static/grapes.png"/>]

image1.name
#returns 'img'

image1["src"]
#returns '/static/dionysus.jpg'

image2["src"]
#returns '/static/grapes.png'

soup.title
#returns <title>Profile: Dionysus</title>

soup.title.string
#returns 'Profile: Dionysus'

soup.find_all("img", src="/static/dionysus.jpg")
#returns [<img src="/static/dionysus.jpg"/>]
'''

base_url = "http://olympus.realpython.org"
html_page = urlopen(base_url + "/profiles")
html_text = html_page.read().decode("utf-8")

soup = BeautifulSoup(html_text, "html.parser")

#soup.find_all("a") returns a list of all the links in the HTML source. 
# You can loop over this list to print out all the links on the web page:
for link in soup.find_all("a"):
    link_url = base_url + link["href"]
    print(link_url)
#You can access the relative URL for each link through the "href" subscript. 
# Concatenate this value with base_url to create the full link_url.