def myfunction(x):
    print("hello" + "\t" + x,"okay")

myfunction("rishi")

class myclass:
    def __init__(self, fname, lname):
        self.fn = fname
        self.ln = lname

    def greet(self): #The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.It does not have to be named self , you can call it whatever you like, but it has to be the first parameter of any function in the class:
        print("Welcome " + self.fn)

o1 = myclass("Rishi","Gautam")

print("Hello",o1.fn,o1.ln)
o1.fn = "RRAJ"
o1.greet()


mydictvar = {
    "name": "bob",
    "country": "nepal"
}

mylistvar = ["bob","nepal", "26"] # list == array

""" mulitline comments
List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered and unindexed. No duplicate members.
Dictionary is a collection which is unordered and changeable. No duplicate members.
"""