"""The '__init__'  method is usedd to initialize the object's attributes after
the object of the class is created.
-'__init__' is aspecial method in Python classes.
-'__init__' is automatically called when you create a new instance of a class.
- It enables you to set up the object according to your specific requirements
during the object's creation.
"""
# The syntax of the __init__ method can be written as following.


class SomeClass:
    def __init__(self, arg1, arg2):
        # constructor body
        self.arg1 = arg1
        self.arg2 = arg2


# self - is an instance of the class, Mandatory.
# arg1 and arg2 - are the parameters. We can pass as many parameters as we want
# or the field can also be left empty.
# Python constructor(__init__) can be created with of without any parameters.
# Default __init__ constructor.
# A constructor created without parameters other than self(a reference to the
# instance being constructed) is called the default constructor.
class SomeClass:
    def __init__(self):
        # constructor body
        self.arg1 = "It is a default value for arg1"
        self.arg2 = "It is a default value for arg2"


# __init__ with parameters
class Vehicle:
    def __init__(self, name, model):
        self.name = name
        self.model = model

    def vehicle(self):
        print(f'Brand: {self.name} and model: {self.model}')


bmw_car = Vehicle('BMW', 'X5')
audi_car = Vehicle('Audi', 'A4')

bmw_car.vehicle()
audi_car.vehicle()
"""The __call__ method. When we invoke a function, we simply use the function
name with parenthesis, such function(), to notify interpreter that a function
is being called. When we invoke a function in Python, the interpreter executes
the __call__ method in the background.
"""


def func(a, b):
    print(a + b)


func(32, 8)
func.__call__(8, 9)


# __call__ inside Python classes
# The concept behind using __call__  is to call the instance of the classes as
# if they were a function.
class Demo:
    def __init__(self):
        print('Hello from constructor.')

    def __call__(self):
        print('Hello from call.')


example = Demo()
example()


# __call__ with parameters
class Student:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __call__(self, school):
        print(f'The id of {self.name} is {self.id}.')
        print(f'The school name is {school}.')


detail = Student(45, 'Sachin')
detail('GSS')
