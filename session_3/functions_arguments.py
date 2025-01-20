# Types of Python Function Arguments:
# Default arguments
# Keyword arguments(named arguments)
# Positional arguments
# Arbitrary arguments(variable-length arguments *args and *kwargs)

# Python program to demonstrate default arguments
def myFun(a, b = 25):
    print("a:", a)
    print("b:", b)


myFun(10)

# Python program to demonstrate Keyword Arguments
def employee(firstname, position):
    print(firstname, position)

employee(firstname = "Greek",position="hacker")
employee(firstname = "Abby", position = "singer")


# Python program to demonstrate Positional Arguments
def nameAge(name, age):
    print("Hi, I'm", name)
    print("My age is", age)

# You'll get correct output because
# arguments is given in order
print("Case - 1:")
nameAge("R2D2", 34)
# You'll get incorrect output because
# argument is not in order
print("\nCase - 2:")
nameAge(34, "R2D2")
print()

# Arbitrary Keyword Arguments
# *args - Non-Keyword Arguments
# *kwargs - Keyword Arguments

# Python program to illustrate
# *args for variable number of arguments
def myFun(*argv):
    for arg in argv:
        print(arg)

myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks!')
print()
# Python program to illustrate
# *kwargs for variable number of keyword arguments
def myFun(**kwargs):
    for key, value in kwargs.items():
        print("%s == %s" %(key, value))

# Driver code
myFun(first = 'Geeks', mid = 'for', last = 'Geeks!')
print()

# Docstring is the first string after the function is called.
# This is used to describe the functionality of the function.
def evenOdd(x):
    """Function to check if the number is even or odd."""
    if (x % 2 == 0):
        print("even")
    else:
        print("odd")
    
print(evenOdd.__doc__)

# Python Function within Functions
# Python program to
# demonstrate accessing of
# variables of nested functions
def f1():
    s = 'I love Geeks!'
    
    def f2():
        print(s)
    
    f2()

# Driver's code
f1()