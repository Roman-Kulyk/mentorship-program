def counting_out(max_count):
    count = 1
    while count <= max_count:
        yield count
        count += 1


for i in counting_out(5): print(i)


def fibo_generator(max_count):
    """This is a function that generates list of Fibonacci numbers."""
    if max_count >= 1:
        yield 1
    if max_count >= 2:
        yield 1
    first, second = 1, 2
    count = 3
    while count <= max_count:
        yield second
        first, second = second, first + second
        count += 1


f_gen = fibo_generator(25)
print(list(f_gen))


def fibo_generator(max_count):
    """This is a function that generates list of Fibonacci numbers."""
    first, second = 0, 1
    for _ in range(max_count):
        yield second
        first, second = second, first + second


f_gen = fibo_generator(10)
print(type(f_gen))
print(list(f_gen))
