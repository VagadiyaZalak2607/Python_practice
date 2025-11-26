thisset = {"apple", "banana", "cherry","apple","Cherry",True,1,2}
tropical = {"pineapple", "mango", "papaya"}
print(thisset)

#length of set
print(len(thisset))

#type of set
print(type(thisset))

#loop in set
for x in thisset:
    print(x)

#add items
thisset.add("orange")
print(thisset)

#update set
thisset.update(tropical)
print(thisset)

#remove item from set
thisset.remove("Cherry")
print(thisset)

#delete item
x = thisset.pop()
print(x)
print(thisset)