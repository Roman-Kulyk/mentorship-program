a = 23
b = 230
if b > a:
    print("b is greater than a")

if b > a:print("b is greater than a")
print()

x = 35
y = 35
if x > y:
    print("x is greater than y")
elif x == y:
    print("x and y are equal")

z = 250
v = 33
if v > z:
    print("z is greater than v")
else:
    print("v is not greater than z")
print("z is greater than v") if z > v else print("z is not greater than v")
print()

a = 230
b = 230
print("A") if a > b else print("=") if a == b else print("B")
#And
a = 300
b = 44
c = 600
if a > b and c > a:
    print("Both conditions are True.")
print()
#Or
a = 300
b = 44
c = 600
if a > b or a > c:
    print("At least one conditions is True")
print()
#Not
a = 44
b = 300
if not a > b:
    print("a is NOT greater than b")
print()
#Neste If
x = 61
if x > 30:
    print("Above thirty!,")
    if x > 40:
        print("and also above forty!")
    else:
        print("but not above forty!")
print()
#pass
a = 45
b = 568
if b > a:
    pass#it does nothing