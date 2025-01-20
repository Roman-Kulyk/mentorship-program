###############################################################################
def fibo_generator(number):
    """This is a function that generates list of Fibonacci numbers."""
    if number >= 1:
        yield 1
    if number >= 2:
        yield 1
    n1, n2 = 1, 2
    count = 3
    while count <= number:
        yield n2
        n1, n2 = n2, n1 + n2
        count += 1


f_gen = fibo_generator(10)
print(f_gen)
# print(next(f_gen))
# print(next(f_gen))
# print(next(f_gen))
# print(next(f_gen))
# print(next(f_gen))
# print(next(f_gen))
# print(next(f_gen))
# print(next(f_gen))
# print(next(f_gen))
# print(next(f_gen))
#print(next(f_gen))
print(list(f_gen))
print()

###############################################################################
def fibo_generator(number):
    """This is a function that generates list of Fibonacci numbers."""
    n1, n2 = 0, 1
    for _ in range(number):
        yield n2
        n1, n2 = n2, n1 + n2


f_gen = fibo_generator(10)
print(f_gen)
# print(next(f_gen))
# print(next(f_gen))
# print(next(f_gen))
# print(next(f_gen))
# print(next(f_gen))
# print(next(f_gen))
# print(next(f_gen))
# print(next(f_gen))
# print(next(f_gen))
# print(next(f_gen))
#print(next(f_gen))
print(list(f_gen))
print()

###############################################################################
class IteratorFib():
    """This is a class that generates list of Fibonacci numbers."""
    def __init__(self, number):
        self.n1 = 0
        self.n2 = 1
        self.c = 0
        self.number = number

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.c == 0:
            self.c += 1
            return 0
        self.n1, self.n2 = self.n2, self.n1 + self.n2
        self.c += 1
        if self.c > self.number:
            raise StopIteration
        return self.n1
    
fib1 = IteratorFib(10)
print(fib1)
# print(next(fib1))
# print(next(fib1))
# print(next(fib1))
# print(next(fib1))
# print(next(fib1))
# print(next(fib1))
# print(next(fib1))
# print(next(fib1))
# print(next(fib1))
# print(next(fib1))
# print(next(fib1))
print(list(fib1))