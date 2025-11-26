thislist = ["apple", "banana", "cherry"]
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
print(thislist)

#length of list
print(len(thislist))

#type of list
print(type(list1))
print(type(list2))
print(type(list3))

#slicing
print(thislist[1])
print(thislist[2:5])

#update list
thislist[1] = "blackcurrant"
print(thislist)

#insert item 
thislist.insert(2, "watermelon")
print(thislist)

#insert item 
thislist.append("orange")
print(thislist)
thislist.insert(1, "orange")
print(thislist)

#adds two lists
thislist.extend(list2)
print(thislist)

#copy list
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

#add list
list4 = list1 + list2
print(list4)