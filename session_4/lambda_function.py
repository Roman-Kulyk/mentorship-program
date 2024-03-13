"""Python Lambda
A lambda function is a small anonymoue function.
A lambda function can take any number of arguments, but can only have one
expression.
Syntax
lambda arguments: expression
The expression is executed and the result is returned.
"""
# Add 10 to argument a, and return the result.
x = lambda a: a + 10
print(x(5))

# Multiply argument a with argument b and return the result.
x = lambda a, b: a * b
print(x(5, 6))

# Summirize arguments a, b, and c and return the result
x = lambda a, b, c: a + b + c
print(x(5, 6, 2))

"""Why Use Lambda Functions?
The power of lambda is better shown when you use them as an anonymous function
inside another function.
Say you have a definition that takes one argument, and that argument will be
be multiplied with an unknown number.
"""


def myfunc(n):
    return lambda a: a * n


mydoubler = myfunc(2)
print(mydoubler(11))


mytripler = myfunc(3)
print(mytripler(11))

add = lambda x, y: x + y
print(add(7, 8))
# It is not necessary to addign lambda function to variable
print((lambda x, y: x + y)(5, 12))

months = [(1, 'January'), (9, 'September'), (7, 'July'), (4, 'March')]
print(sorted(months, key=lambda x: x[1]))
print(sorted(months))
