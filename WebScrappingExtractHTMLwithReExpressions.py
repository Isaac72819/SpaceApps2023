# regex_soup.py

import re
from urllib.request import urlopen

'''
url = "http://olympus.realpython.org/profiles/dionysus"
page = urlopen(url)
html = page.read().decode("utf-8")

pattern = "<title.*?>.*?</title.*?>"

#<title.*?> matches the opening <TITLE > tag in html. The <title part of the 
# pattern matches with <TITLE because re.search() is called with re.IGNORECASE, 
# and .*?> matches any text after <TITLE up to the first instance of >

#.*? non-greedily matches all text after the opening <TITLE >, stopping at the 
# first match for </title.*?>

#</title.*?> differs from the first pattern only in its use of the / character, 
# so it matches the closing </title  / > tag in html

match_results = re.search(pattern, html, re.IGNORECASE)
title = match_results.group()
title = re.sub("<.*?>", "", title) # Remove HTML tags
#The second regular expression, the string "<.*?>", also uses the non-greedy .*? 
# to match all the HTML tags in the title string. By replacing any matches with "", 
# re.sub() removes all the tags and returns only the text.

print(title)
'''

url = "http://olympus.realpython.org/profiles/dionysus"
html_text = urlopen(url).read().decode("utf-8")

for string in ["Name: ", "Favorite Color:"]:
    string_start_index = html_text.find(string)
    text_start_idx = string_start_index + len(string)
    
    next_html_tag_offset = html_text[text_start_idx:].find("<")
    text_end_idx = text_start_idx + next_html_tag_offset
    
    raw_text = html_text[text_start_idx : text_end_idx]
    clean_text = raw_text.strip(" \r\n\t")
    print(clean_text)
    
#1-You use html_text.find() to find the starting index of the string, 
# either "Name:" or "Favorite Color:", and then assign the index to string_start_idx.

#2-Since the text to extract starts just after the colon in "Name:" or 
# "Favorite Color:", you get the index of the character immediately 
# after the colon by adding the length of the string to start_string_idx, 
# and then assign the result to text_start_idx.

#3-You calculate the ending index of the text to extract by determining the 
# index of the first angle bracket (<) relative to text_start_idx and assign 
# this value to next_html_tag_offset. Then you add that value to 
# text_start_idx and assign the result to text_end_idx.

#4-You extract the text by slicing html_text from text_start_idx to text_end_idx 
# and assign this string to raw_text.

#5-You remove any whitespace from the beginning and end of raw_text using 
# .strip() and assign the result to clean_text.