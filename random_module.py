# This code uses the random module to select a random element from the list 
# using the random.choice() function
import random
list_1 = [4, 5, 6, 7, 8, 9]
print(random.choice(list_1))
print()
# This code uses the random module to generate random integers within specific
# ranges.
import random
v1 = random.randint(7, 17)
print("Random number between 7 and 17 is %s" %(v1))
v2 = random.randint(-15, -7)
print("Random number between -15 and -7 is %s" %(v2))
print()
# This code uses the random function from the 'random' module. It prints a 
# random floating-point number between 0 and 1 when you call random().
from random import random
print(random())
print()
# This code uses the random.choice() function from the random module to randomly
# select element from different data types.
import random
list1 = [2,3,4,5,6,7]
print(random.choice(list1))
string = "punch"
print(random.choice(string))
tuple1 = (4,5,6,7,8,)
print(random.choice(tuple1))
print()
# This code uses the random.shuffle() function from the 'random' module to 
# shuffle the elements of a list.
import random
sample_list = ['a', 'b', 'c', 'd', 'e']
print('Original list: ')
print(sample_list)
random.shuffle(sample_list)
print('\nAfter the first shuffle:')
print(sample_list)
random.shuffle(sample_list)
print('\nAfter the second shuffle:')
print(sample_list)
print()
# The choices() method returns multiple random elements from the list with
# replacement. You can weigh the possibility of each result with weights
# parameter  or the cum_weights parameter.
import random
my_list = ['geeks', 'for', 'python']
print(random.choices(my_list, k = 4))
print()
my_list = ['geeks', 'for', 'python']
print(random.choices(my_list, weights = [5,1,1],k = 4))
print()
# The randrange() method choose a random item from range(stop) or (start, stop
# [, step]).
print(random.randrange(0, 100, 5))