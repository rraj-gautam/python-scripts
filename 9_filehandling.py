#f = open("filehandling.txt")
# similar to f = open("filehandling.txt", "rt")

"""
"r" - Read - Default value. Opens a file for reading, error if the file does not exist

"a" - Append - Opens a file for appending, creates the file if it does not exist  # append to end of file

"w" - Write - Opens a file for writing, creates the file if it does not exist #overwrite existing content

"x" - Create - Creates the specified file, returns an error if the file exists

"t" - Text - Default value. Text mode

"b" - Binary - Binary mode (e.g. images)
"""
# f.write("hello file")

"""
print(f.read())
#print(f.readline())
f.close()
"""

f = open("filehandling.txt", "w")
f.write("Hello File Handling")
f.close()
f = open("filehandling.txt", "r")
print(f.read())
f.close()

####### To delete file, OS module needs to be imported ########
"""
import os
os.remove("filehandling.txt")
"""
import os
# now check if file exists
if os.path.exists("filehandling.txt"):
    print("removing file")
    os.remove("filehandling.txt")
else:
    print("File doesnot exists")    

# os.mkdir("createFolder")
# os.rmdir("createFolder")