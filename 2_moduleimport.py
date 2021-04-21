import first    # my module
#import first as ft             # ft.myfunction("ITONICS")
#from first import mydictvar   # When importing using the from keyword, do not use the module name when referring to elements in the module. Example: person1["age"], not mymodule.person1["age"]
import platform # built in module
import sys

#first
first.myfunction("ITONICS")

a = first.mydictvar["country"]
print(a)

print(first.mylistvar[1])
#############################################
print(platform.python_version())
print(sys.version_info)

x = dir(platform)
print(x)



