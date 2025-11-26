thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict1 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
thisdict2 = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
}
print(thisdict)
print(thisdict["brand"])
print(thisdict1)

#length of dict
print(len(thisdict))

print(thisdict2)

#type of dict
print(type(thisdict))

#value of specified key
x = thisdict.get("brand")
print(x)

#kyes of dict
y = thisdict.keys()
print(y)

#add dict
thisdict2["color"] = "black"
z = thisdict2.keys()
print(z)

#update dict
thisdict2["year"] = 2020
print(thisdict2)

#removes element
thisdict.pop("model")
print(thisdict)

#copy dict
mydict = thisdict.copy()
print(mydict)