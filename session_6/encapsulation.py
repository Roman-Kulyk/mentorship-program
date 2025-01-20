"""Encapsulation is one of the fundamental concepts in OOP. It describes the
idea of wrapping data and the methods that work on data within one unit. This
put restrictions on accessing variables and methods directly and can prevent
the accidental modification of data. To prevent accidental change, an object's
variable can only be changed by an object's method. Those types of variables
are known as private variables.
A class is an example of encapsulation as it encapsulates all the data that is
member functions, variables, etc. The goal of information  hiding is to ensure
that an object's state is always valid by controlling access to attributes that
are hidden from the outside world.
"""
# Protected members are those members of the class than cannot be accessed
# outside the class but can be accessed from within the class and it subclasses
# To acomplish- this in Python, just follow the convention by prefixing the
# name of the member by a single underscore'_'.


class Base:
    def __init__(self):
        self._a = 2


class Derived(Base):
    def __init__(self):
        Base.__init__(self)
        print("Calling protected member of base class: ",
              self._a)

        self._a = 3
        print("Calling modified protected member outside class: ",
              self._a)


obj1 = Derived()

obj2 = Base()

print("Accessing protected member of obj1: ", obj1._a)
print("Accessing protected member of obj2: ", obj2._a)
# Private members are similar to protected members, the difference is that the
# class members declared private should neither be accessed outside the class
# not by any base class. In Python, there is no existence or Privat instance
# variables that cannot be accessed except inside a class. However, to define a
# private member prefix the member name with double underscore '__'.


class Base:
    def __init__(self):
        self.a = 'GeeksforGeeks'
        self.__c = 'Geeksforgeeks'


class Derived(Base):
    def __init__(self):
        print('Calling private member of base class: ')
        print(self.__c)


obj1 = Base()


print(obj1.a)
print(obj1.c)
# obj2 = Derived()
