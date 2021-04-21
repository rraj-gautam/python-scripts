#pip3 install camelcase   has been done before hand
# pip3 list to list all packages

import camelcase

c = camelcase.CamelCase()
txt = "Hello world"
print(c.hump(txt))
#This method capitalizes the first letter of each word.