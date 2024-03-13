cars = ["BMW","VW","Opel"]
for x in cars:#is used for iterating over a sequence
    print(x)
print()
for i in "apple":
    print(i)
print()
cars = ["BMW","VW","Opel","Mercedes"]
for x in cars:#is used for iterating over a sequence
    print(x)
    if x == "Opel":
        break
print()

for x in cars:#is used for iterating over a sequence
    if x == "VW":
        continue
    print(x)
print()
#Range() function
for x in range(5):
    print(x)
print()
for x in range(2,7):
    print(x)
print()
for i in range(4,34,4):
    print(i)
print()
for x in range(5):
    print(x)
else:
    print("Finally finished!")
print()
for x in range(5):
    if x == 3: break
    print(x)
else:
    print("Finally finished!")
print()
print(type(range(5)))
print()
colors = ["red","yellow","black"]
cars = ["Ferarri","Lamborgini","Mazeratti"]
for x in colors:
    for y in cars:
        print(x,y)
print()
for y in [3,4,5]:
    pass
