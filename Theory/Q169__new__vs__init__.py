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

Differences Between __init__ and __new__:
__init__ is an instance method, while __new__ is a static method.
__new__ is responsible for creating and returning a new instance (object), 
while __init__ is responsible for initializing the attributes of the newly created object.
__new__ is called before __init__.
__new__ happens first, then __init__.
__new__ can return any object, while __init__ must return None.
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
