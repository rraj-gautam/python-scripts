import json

###### from json to python standard ############################
#json lines:
x = '{"name": "alice", "age": "20"}'

#parse x
y = json.loads(x)
#result is a python dictionary

print(y["age"])

###### from python to json standard #######################
#python object (dict)
x = {
    "name": "bob",
    "age": "30"
}

#convert to JSON
y = json.dumps(x)
print(y)

z = json.dumps(x,indent=4, separators=(",","="), sort_keys=True)
print(z)

"""
You can convert Python objects of the following types, into JSON strings:
dict
list
tuple
string
int
float
True
False
None
"""
print(json.dumps(["apple","100"]))
print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))
