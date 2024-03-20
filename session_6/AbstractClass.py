"""Abstract classes are classes than contain one or more abstract methods. An
abstract method is a method that is declared, but contains no implementation.
Abstract classes cannot be instantiated, and require subclasses to provide
implementations for the abstract methods.
"""


# class AbstractClass:

#     def do_something(self):
#         pass


# class B(AbstractClass):
#     pass


# a = AbstractClass()
# b = B()
"""In fact, Python on its own doesn't provide abstract classes. Yet, Python
comes with a module which provides the infrastructure for defining Abstract
Base Classes(ABCs). This module is called - for obvious reasons -abc.
"""
from abc import ABC, abstractmethod


class AbstrctClassExample(ABC):

    def __init__(self, value):
        self.value = value
        super().__init__()

    @abstractmethod
    def do_something(self):
        pass

# class DoAdd42(AbstrctClassExample):
#     pass

# x = DoAdd42(4)

# # We get an exception that DoAdd42 can't be instantiated.
# # We will do it in correct way in the following example, in which we define
# # two classes inheriting from our abstract class


class DoAdd42(AbstrctClassExample):

    def do_something(self):  # this is an example of polymorphism...
        return self.value + 42


class DoMu142(AbstrctClassExample):

    def do_something(self):  # we have two methods with the same name^^^
        # doing different things
        return self.value * 42

# A class that is derived from an abstract class cannot be instantiated unless
# all of its abstract methods are overriden.


x = DoAdd42(10)


y = DoMu142(10)

print(x.do_something())
print(y.do_something())

###############################################################################


class AbstractClassExample(ABC):

    @abstractmethod
    def do_something(self):
        print('Some implementation!')
# An abstract- method can have an implementation in the abstract class! Even
# if they are implemented, designers of subclassed will be forced to override
# the iplementation.


class AnotherSubclass(AbstractClassExample):

    def do_something(self):
        super().do_something()
        print('The enrichment from AnotherSubclass')


x = AnotherSubclass()
x.do_something()
