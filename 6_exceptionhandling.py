#The try block will generate an error, because x is not defined

try:
    print(x)
except:
    print("exception occured")
else:
    print("going good")
#The finally block, if specified, will be executed regardless if the try block raises an error or not
finally:
    print("exception has been handled")

#Try to open and write to a file that is not writable:
#The try block will raise an error when trying to write to a read-only file:
"""
try:
    f = open("noexistsfile.txt")
    f.write("passwords are safe here")
except:
    print("writing file went wrong")
finally:
    f.close()        
"""
#The program can continue, without leaving the file object open    

############# Raise an exception #############

x = -1
if x < 0:
    raise Exception("no numbers below 0")

if not type(x) is str:
    raise TypeError("only string allowed")    