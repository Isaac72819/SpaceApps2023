import re
re.findall("ab*c", "ac") # returns ['ac'] / * stands for zero or more times of what comes before it / findall to find any string that matches the given expression
#The first argument of re.findall() is the regular expression that you want to match, 
# and the second argument is the string to test.

#The regular expression "ab*c" matches any part of the string that begins with "a", 
# ends with "c", and has zero or more instances of "b" between the two. re.findall() 
# returns a list of all matches. The string "ac" matches this pattern, so it’s returned 
# in the list.

re.findall("ab*c", "abcd")
#returns ['abc']

re.findall("ab*c", "acc")
#returns ['ac']

re.findall("ab*c", "abcac")
#returns ['abc', 'ac']

re.findall("ab*c", "abdc")
#returns [] = .findall() returns an empty list when no matches are found

re.findall("ab*c", "ABC")
#returns [] = findall() is case sensitive

re.findall("ab*c", "ABC", re.IGNORECASE)
#returns ['ABC']

#You can use a period (.) to stand for any single character in a regular expression. 
# For instance, you could find all the strings that contain the letters "a" and "c" 
# separated by a single character as follows:
re.findall("a.c", "abc")
#returns ['abc']

re.findall("a.c", "abbc")
#returns []

re.findall("a.c", "ac")
#returns []

re.findall("a.c", "acc")
#returns ['acc']


#you can use "a.*c" to find every substring that starts with "a" and ends with "c", 
# regardless of which letter—or letters—are in between:
re.findall("a.*c", "abc")
#returns ['abc']

re.findall("a.*c", "abbc")
#returns ['abbc]

re.findall("a.*c", "ac")
#returns ['ac']

re.findall("a.*c", "acc")
#returns ['acc']

# you use re.search() to search for a particular pattern inside a string
match_results = re.search("ab*c", "ABC", re.IGNORECASE)
match_results.group()
#returns 'ABC'

#re.sub(), which is short for substitute, allows you to replace the text 
#in a string that matches a regular expression with new text.
string = "Everything is <replaced> if its in <tags>."
string = re.sub("<.*>", "ELEPHANTS", string)
string
#returns 'Everything is ELEPHANTS.'

#PYTHON be greedy and it only picked up the longest string, so we gotta add *?
#so it matched with the shortest string too
string = "Everything is <replaced> if its in <tags>."
string = re.sub("<.*?>", "ELEPHANTS", string)
string
#returns 'Everything is ELEPHANTS if its in ELEPHANTS.'

#This time, re.sub() finds two matches, <replaced> and <tags>, and substitutes 
#the string "ELEPHANTS" for both matches.