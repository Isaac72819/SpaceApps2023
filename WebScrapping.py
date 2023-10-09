from urllib.request import urlopen

# Afrodite = url = "http://olympus.realpython.org/profiles/aphrodite"
url = "http://olympus.realpython.org/profiles/poseidon"

page = urlopen(url) #pass to urlopen

#print(page)

html_bytes = page.read()#to extract the text in HTML format
html = html_bytes.decode("utf-8")#converts bytes to string using utf-8
#html = page.read().decode("utf-8")

#print(html)

# Afrodite = title_index = html.find("<title>")
#print(title_index) = 14
title_index = html.find("<title >") #.find() returns the index of the first occurrence of the substring, or title in this case


# Afrodite = start_index = title_index + len("<title>")
#print(start_index) = 21
start_index = title_index + len("<title >") #to get the length of the entire title


end_index = html.find("</title>") # to get the index of the closing title tag
#print(end_index) = 39

title = html[start_index:end_index] #to get the title by slicing the html
print(title) #= 'Profile of Afrodite'