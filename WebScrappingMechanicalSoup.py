import mechanicalsoup #to interact with the website

#Browser objects represent the headless web browser
browser = mechanicalsoup.Browser()

#You can use them to request a page from the Internet by passing a URL to their .get() method:
url = "http://olympus.realpython.org/login"

"""
page = browser.get(url)

#page is a Response object that stores the response from requesting the URL from the browser:
page
#returns <Response [200]>

#MechanicalSoup uses Beautiful Soup to parse the HTML from the request, and page has a .soup attribute that represents a BeautifulSoup object:
type(page.soup)
#returns <class 'bs4.BeautifulSoup'>

#You can view the HTML by inspecting the .soup attribute:
page.soup
#returns 
# <html>
# <head>
# <title>Log In</title>
# </head>
# <body bgcolor="yellow">
# <center>
# <br/><br/>
# <h2>Please log in to access Mount Olympus:</h2>
# <br/><br/>
# <form action="/login" method="post" name="login">
# Username: <input name="user" type="text"/><br/>
# Password: <input name="pwd" type="password"/><br/><br/>
# <input type="submit" value="Submit"/>
# </form>
# </center>
# </body>
# </html>
"""

'''
login_page = browser.get(url)
login_html = login_page.soup

form = login_html.select("form")[0]
form.select("input")[0]["value"] = "zeus"
form.select("input")[1]["value"] = "ThunderDude"

profiles_page = browser.submit(form, login_page.url)

profiles_page.url
#returns 'http://olympus.realpython.org/profiles'

#1-You create a Browser instance and use it to request the URL http://olympus.realpython.org/login. 
# You assign the HTML content of the page to the login_html variable using the .soup property.

#2-login_html.select("form") returns a list of all <form> elements on the page. Because the page has
# only one <form> element, you can access the form by retrieving the element at index 0 of the list. 
# When there is only one form on a page, you may also use login_html.form. The next two lines select 
# the username and password inputs and set their value to "zeus" and "ThunderDude", respectively.

#3-You submit the form with browser.submit(). Notice that you pass two arguments to this method, the form 
# object and the URL of the login_page, which you access via login_page.url.


#Now that you have the profiles_page variable set, it’s time to programmatically obtain the URL for each
# link on the /profiles page.
links = profiles_page.soup.select("a")

for link in links:
    address = link["href"]
    text = link.text
    print(f"{text} : {address}")
    
#Aphrodite: /profiles/aphrodite
# Poseidon: /profiles/poseidon
# Dionysus: /profiles/dionysus

base_url = "http://olympus.realpython.org"
for link in links:
    address = base_url + link["href"]
    text = link.text
    print(f"{text}: {address}")
    
#Aphrodite: http://olympus.realpython.org/profiles/aphrodite
# Poseidon: http://olympus.realpython.org/profiles/poseidon
# Dionysus: http://olympus.realpython.org/profiles/dionysus
'''

login_page = browser.get(url)
login_html = login_page.soup

form =login_html.form
form.select("input")[0]["value"] = "zeus"
form.select("input")[1]["value"] = "ThunderDude"

profiles_page = browser.submit(form, login_page.url)

print(profiles_page.soup.title)