mylist = ["apple","ball","cat","dog","ear"]
print(mylist[-1]) # -1 is last index and -2 is second last
print(mylist[0:2]) #prints index 0,1
print(mylist[:4])  #prints from begining to index 3(excludes index 4)
print(mylist[3:])


# replace values
mylist[1]="basketball"
print(mylist)    

mylist[1:2]=["basketball","football","volleyball"]
print(mylist)  

mylist.insert(2,"handball")
print(mylist)

#add items
mylist.append("nose")
print(mylist)  

mylist.insert(0,"mango")
print(mylist)  

#extend
newlist=["hell","heaven"]
mylist.extend(newlist)
print(mylist)  


#remove
mylist.remove("hell")
print(mylist)  

mylist.pop() #removes last one
print(mylist)  

mylist.pop(0)
print(mylist)  

del mylist[8]
print(mylist)  


print(newlist)  
newlist.clear() #empties list
print(newlist) 

del newlist #deletes entire list
#print(newlist)  #gives error


print("\n", "############################################################ \n")

#conditions and loops
if "ball" in mylist:
    print("you are football fan")

for i in mylist:
    print(i)
print("--------------")
#loop through the list items by referring to their index number.
for i in range(len(mylist)):  #len=8, range, 0-7 . So loop will go from 0 to 7
    print(mylist[i])
print("--------------")

j=0
while j<len(mylist):
    print(mylist[j])
    j=j+1
print("--------------")

for i in range(10):
    print(i)


"""
Method	    Description
append()	Adds an element at the end of the list
clear()	    Removes all the elements from the list
copy()	    Returns a copy of the list
count()	    Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	    Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	    Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()      Sorts the list
"""    