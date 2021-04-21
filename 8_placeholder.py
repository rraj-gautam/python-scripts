x = 25
txt = "your age is {} years"
print(txt.format(x))

#You can add parameters inside the curly brackets to specify how to convert the value:
quantity = 3
itemno = 567
price = 49
myorder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(quantity, itemno, price))

neworder = "I want {0} kg of rice for {2} dollars with quality index {0}"
print(neworder.format(quantity,itemno,price))
