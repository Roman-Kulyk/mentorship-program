# This code uses 'random' module to generate random integers between the given
# ranges. Return random integer in range [a, b] including both end points.
import random
n1 = random.randint(5, 15)
print("Random number between 5 and 15 is %s" %(n1))
n2 = random.randint(-43, -23)
print("Random number between -43 and -23 is %s" %(n2))
print()
# The randrange(star, stop[,step]) returens a randomy selected element from
# range(stop) or range(stat, stop, step)
import random
print(random.randrange(9))
from random import randrange
print(randrange(3,23,2))
print()
# The random() method from the random module generates a float number between 0
# and 1
import random
print(random.random())
print()
# The random.choice() function from the random module randomly selects elements
# from different data types.
import random
play_list1 = [2, 4, 6, 8, 10]
print(random.choice(play_list1))
string = 'Freeks'
print(random.choice(string))
car_tuple = ('vw', 'BMW', 'GM')
print(random.choice(car_tuple))
print()
# The choises() method returns multiple random elements from the list with
# replacement. You can weigh the possibility of each result with weights
# parameter or the cum_weights parameter. The element can be a string, a range,
# a list, a tuple or any other kind of sequece.
import random
mylist = ['geeks', 'for', 'python']
print(random.choices(mylist, weights = [10, 1, 1], k = 5))
print()
# This code uses the random.shuffle() function from the 'random' module to
# shuffle the elements of a list.
import random
sample_list =[1, 3, 5, 'a', 'c', 'e']
print('Original list:- ')
print(sample_list)
random.shuffle(sample_list)
print('\nAfter the first shuffle: ')
print(sample_list)
random.shuffle(sample_list)
print('\nAfter the second shuffle: ')
print(sample_list)