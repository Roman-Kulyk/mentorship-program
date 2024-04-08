import math


class Numbers:
    # It is a method for creating and returning a new instance of the class
    def __new__(cls, number):
        instance = super().__new__(cls)
        return instance

    # It is a method for initializing the newly created object
    def __init__(self, number):
        self.number = number

    # It is a method to print a list which contains simple positive numbers
    def __call__(self):
        number_list = []
        p = 2
        while len(number_list) != self.number:
            if (math.factorial(p-1)+1) % p == 0:
                number_list.append(p)
            p += 1
        print(f'First {self.number} numbers in list are: {number_list}')

    # It is a method to count summ of list numbers
    def sum_count(self):
        number_list = []
        p = 2
        while len(number_list) != self.number:
            if (math.factorial(p-1)+1) % p == 0:
                number_list.append(p)
            p += 1
            amount = sum(number_list)
        print(f"The total amount of lists numbers is: {amount}")


# Declaration of instance of class Numbers
x = Numbers(5)
x()  # Call the instance of the classes as if they were a function
x.sum_count()
print()
# Declaration of another instance of class Numbers
y = Numbers(15)
y()  # Call the instance of the classes as if they were a function
y.sum_count()
