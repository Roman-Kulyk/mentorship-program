"""
__new__ is a static method that's responsible for creating and
returning a new instance of the class. It takes the class as its first argument
followed by additional arguments.
You should use __new__ when you need to control the creation of the object. For
example, you might want to use __new__ to:

-Ensure that the object is of certain type.
-Set the object initial state.
-Prevent the object from being created.

__init__ is an instance method that is responsible for initializing the newly
created object. It takes the object as int first argument followed by
additional arguments.
You should use __init__ when you need to initialize the object. For example,
you might want to use __init__ to:

-Set the object's attributes.
-Call the objects superclass' __init__ methos.
-Perform other initialization tasks.
"""
# https://builtin.com/data-science/new-python


class Person:
    def __new__(cls, name, age):
        print('Creating a new Perspon object.')
        instance = super().__new__(cls)
        return instance

    def __init__(self, name, age):
        print('Initializing the Person object')
        self.name = name
        self.age = age


person = Person('John Doe', 30)
print(f"Person's name: {person.name}, age: {person.age}")
