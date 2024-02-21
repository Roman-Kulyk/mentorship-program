cardict = {
    "brand":"VW",
    "model":"Passat",
    "year":1980,
    "year":1988,#it will overwrite existing value 1980
    "colors":['violet','yellow','black'],
    "electric":True
}
print("Dict is ordered, changeable and do not allow duplicates.")
print(cardict)
print(cardict["brand"])
print(len(cardict))
print(type(cardict))
print()
#the dict() constructor
thedict = dict(name = "R2D2", age = 34, country = "Galaxy Far Far Away")
print(thedict)
print()
#Accessing items
cardict = {
    "brand":"VW",
    "model":"Passat",
    "year":1988,
    "colors":['violet','yellow','black'],
    "electric":True
}
x = cardict["model"]
print(x)
print()
x = cardict.get("model")
print(x)
x = cardict.keys()
print(x)
x = cardict.values()
print(x)
x = cardict.items()
print(x)
if "model" in cardict:
    print("Yes")
print()
#Change values
cardict = {
    "brand":"VW",
    "model":"Passat",
    "year":1988,
    "colors":['violet','yellow','black'],
    "electric":True
}
cardict["year"] = 2018
print(cardict["year"])
cardict.update({"year":2020})
print(cardict["year"])
print()
#Add items
cardict = {
    "brand":"VW",
    "model":"Passat",
    "year":1988,
    "colors":['violet','yellow','black'],
    "electric":True
}
cardict["country"] = "Germany"
print(cardict)
cardict.update({"tyres":"Goodyear"})
print(cardict)
print()
#remove items
cardict = {
    "brand":"VW",
    "model":"Passat",
    "year":1988,
    "colors":['violet','yellow','black'],
    "electric":True
}
cardict.pop("electric")#removes item with the specified key name
print(cardict)
cardict.popitem()#removes the last inserted item
print(cardict)
del cardict["year"]
print(cardict)
cardict = {
    "brand":"VW",
    "model":"Passat",
    "year":1988,
    "colors":['violet','yellow','black'],
    "electric":True
}
cardict.clear()
print(cardict)

del cardict
#print(cardict)#this will cause an error
print()
#Loop Dictionaries
cardict = {
    "brand":"VW",
    "model":"Passat",
    "year":1988,
    "colors":['violet','yellow','black'],
    "electric":True
}
for x in cardict:#print all key names in dict, one by one
    print(x)
print()
for x in cardict:
    print(cardict[x])#print all values in dict, one by one
print()
for x in cardict.values():#returns values of a dict
    print(x)
print()
for x in cardict.keys():#returns keys of a dict
    print(x)
print()
for x,y in cardict.items():#returns keys and values
    print(x,y)
print()
#Copy dictionaries
cardict = {
    "brand":"VW",
    "model":"Passat",
    "year":1988,
    "colors":['violet','yellow','black'],
    "electric":True
}
mydict = cardict.copy()
print(cardict)
print(mydict)
print()
mydict1 = dict(cardict)
print(mydict1)
print()
#Dictionaries method
x = ('key_a', 'key_b', 'key_c')
y = 5
thedict = dict.fromkeys(x,y)
print(thedict)
print()
x = ('key_a', 'key_b', 'key_c')
thedict = dict.fromkeys(x)
print(thedict)

cardict = {
    "brand":"VW",
    "model":"Passat",
    "colors":['violet','yellow','black'],
    "electric":True
}
x =cardict.setdefault("year",1988)
print(x)