#import random   # to make random numbers.
#import statistics #o calculate mathematical statistics of numeric data. like: mean, median
#import pandas  # for data analysing
#import numpy  # for working with arrays, plotting data sets
#import math     # has a set of methods and constants. like: math.sin()
#import json  # to json handling
#import os      # for interacting with OS
#import requests #Make a request to a web page, and print the response text
#import subprocess #to run shell commands
#import logging  # for logging

###################################################################################

import requests #Make a request to a web page, and print the response text like curl
"""
syntaxt:  requests.methodname(params)
-----------------------------------------
delete(url, args)	            Sends a DELETE request to the specified url
get(url, params, args)	        Sends a GET request to the specified url
head(url, args)	                Sends a HEAD request to the specified url
patch(url, data, args)	        Sends a PATCH request to the specified url
post(url, data, json, args)	    Sends a POST request to the specified url
put(url, data, args)	        Sends a PUT request to the specified url
request(method, url, args)	    Sends a request of the specified method to the specified url
"""
x = requests.get("https://sysdaemons.com")
#print(x.text)
print(x.headers)

####################################################################################

import subprocess #to run shell commands
y = subprocess.getoutput("ls -lh")
print(y)

# or , to run shell commands:
import os
os.popen("free -h").read()


####################################################################################

import logging
logging.warning('Watch Out!')   #prints message to console
logging.info('I told you')      #will not print message to console
