import re

txt = "Hello everybody nobody"
x = re.search("^He.*dy$", txt)
print(x)

if x: 
    print("Macthed")
else:
    print("No match")    



x = re.search("body", txt)
print(x)

"""
Function	Description
------------------------------------------------------------------------------
findall	    Returns a list containing all matches
search	    Returns a Match object if there is a match anywhere in the string
split	    Returns a list where the string has been split at each match
sub	        Replaces one or many matches with a string    
"""

y = re.findall("body", txt)
print(y)

z = re.split("\s", txt) # split at every white-space character
print(z)

z = re.split("\s", txt, 1) #split the string at the first white-space character
print(z)

#Replace every white-space character with the tab:
w = re.sub("\s","\t", txt)
print(w)

w = re.sub("body","one", txt)
print(w)

#Replace the first occurrences of a body haracter with one
w = re.sub("body","one", txt, 1)
print(w)


"""
The Match object has properties and methods used to retrieve information about the search, and the result:

.span() returns a tuple containing the start-, and end positions of the match.
.string returns the string passed into the function
.group() returns the part of the string where there was a match
"""

print(x.span())
print(x.string)
print(x.group())