"""Animals are mylticellular, eukaryotic organisms in the biological kingdom
Animalia. With few exceptions, animals consume organic material, breathe
oxygen, have myocytes and are able ot move, can reproduce sexually, and grow
from a hollow sphere of cells, the blastuel, during embryonic development.
"""
from abc import ABC


class Animals(ABC):
    # Here we have first OOP paradigm Abstraction to describe main animal's 
    # function
    def __init__(self, name, age):
        # It is attribute's initialization
        self._name = name  # here encapsulation is used to restrict access
        self._age = age    # to attributes only from subclasses
        super().__init__()

    def eat(self):
        pass

    def breathe(self):
        pass

    def move(self):
        pass

    def reproduce(self):
        pass


# It's an Inheritance paradigm, all following sublasses derived from main class
class Mammals(Animals):
    def move(self):
        print('I can run!!!')

    def reproduce(self):
        print('We give birth to live babies.')

    def breathe(self):
        print("I can breathe only air though my lungs!")

    def eat(self):
        print('I like to eat grass!')


# It is a Polymorphism paradigem which allow to us have method with the same
# name in different subclasse which inhereted the method from main class
class Reptiles(Animals):
    def move(self):
        print('I can glide, crowl, and even jump!!!')

    def reproduce(self):
        print('We produce eggs in the nest.')

    def breathe(self):
        print("I can breathe only air though my lungs!")

    def eat(self):
        print('I like to eat insects, molusks, frogs!')


class Fish(Animals):
    def move(self):
        print('I can swim!!!')

    def reproduce(self):
        print('We are considered to be live-bearing')

    def breathe(self):
        print("I can breathe only air from water!")

    def eat(self):
        print('I like to eat plankton!')


class Birds(Animals):
    def move(self):
        print('I can fly!!!')


class Amphibians(Animals):
    pass


class Invertebrates(Animals):
    pass


class Insects(Animals):
    pass


# It is here to show that attributes are variable which can be accessed throuh
# instances of class
my_pet1 = Mammals('Oskar', 2.5)
my_pet2 = Fish('Goldy', 0.5)
my_pet3 = Reptiles('Tom', 4)


print(f"My second pet's name is {my_pet1._name}. He is {my_pet1._age} years old.")
print(f"My second pet's name is {my_pet2._name}. He is {my_pet2._age} years old.")
print(f"My third pet's name is {my_pet3._name}. He is {my_pet3._age} years old.")
print()
my_pet1.breathe()
my_pet2.breathe()
my_pet3.breathe()
print()
my_pet1.eat()
my_pet2.eat()
my_pet3.eat()
print()
my_pet1.move()
my_pet2.move()
my_pet3.move()
print()
my_pet1.reproduce()
my_pet2.reproduce()
my_pet3.reproduce()
