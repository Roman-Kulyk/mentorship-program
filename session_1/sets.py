cars = {"BMW", "VW", "Opel"}
cars.add("Buick")
print(cars)

x = cars.copy()
print(x)

x.clear()
print(x)

cars2 = {'Mazda','Honda','Toyota','Opel'}
z = cars.difference(cars2)
print(z)

z = cars.intersection(cars2)
print(z)

x = {1,2,3,4,5,6}
y = {1,2,3}
z = y.issubset(x)
print(z)
print()
print(x)
x.pop()
print(x)
print()
x.remove(2)
print(x)
print()
z = x.symmetric_difference(y) 
print(z)
print()
x = {'a','b','c'}
y = {'a','d','e'}
z = x.union(y)
print(z)
print()
x.update(y)
print(x)
print(y)