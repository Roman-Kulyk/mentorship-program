a = 1
while a < 7:#as long as condition is true while loop can execute a set of statements
    print(a)
    a += 1
print()

a = 1 
while a < 7:
    print(a)
    if a == 4:
        break
    a += 1
print()

a = 0 
while a < 7:
    a += 1
    if a == 4:
        continue
    print(a)
print()
a = 1
while a < 7:
    print(a)
    a  += 1
else:
    print("a is no longer less than 7")

print()
x,y = 3,4
print(x,y)
x,y =y,x
print(x,y)