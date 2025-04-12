"""
https://www.datacamp.com/tutorial/python-abstract-classes
What is an Abstract Class?
An abstract class is like a template for other classes. It defines methods that must 
be included in any class that inherits from it, but it doesn’t provide the actual 
code for those methods.

Think of it as a recipe without specific ingredients—it tells you what steps to follow,
but the details depend on the subclass.

Example:
Let’s say you’re building a program to calculate the area of different shapes.

You create an abstract class called Shape that says every shape must have an area() method.
But Shape doesn’t define how area() works—because the formula depends on the type of shape.
Each specific shape (like a Circle or Rectangle) inherits from Shape and provides its own
version of area().
"""
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass

class Car(Vehicle):
    def start_engine(self):
        print("Car engine started")

    def stop_engine(self):
        print("Car engine stopped")

car = Car()
car.start_engine()
car.stop_engine()
