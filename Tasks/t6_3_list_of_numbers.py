
class Numbers:
    def __new__(cls, number):
        instance = super().__new__(cls)
        return instance

    def __init__(self, number):
        self.number = number

    def call(self):
        import math
        number_list = []
        p = 2
        while len(number_list) != self.number:
            if (math.factorial(p-1)+1) % p == 0:
                number_list.append(p)
            p += 1
        print(f'First {self.number} numbers in list are: {number_list}')

    def sum_count(self):
        import math
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
x.call()
x.sum_count()
print()
# Declaration of another instance of class Numbers
y = Numbers(15)
y.call()
y.sum_count()
