import math
number = int(input("Enter your number: "))
number_list = []
p = 2
while len(number_list) != number:
    if (math.factorial(p-1)+1) % p == 0:
        number_list.append(p)
    p += 1
print(number_list)
