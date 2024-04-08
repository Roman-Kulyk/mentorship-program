"""Animals are mylticellular, eukaryotic organisms in the biological kingdom
Animalia. With few exceptions, animals consume organic material, breathe
oxygen, have myocytes and are able ot move, can reproduce sexually, and grow
from a hollow sphere of cells, the blastuel, during embryonic development.
"""
from abc import ABC


class Animals(ABC):
    def __init__(self, name, age=1):
        self.__name = name
        self.__age = age
        self.__total = 1000000
        super().__init__()

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        self.__age = value

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


# It is a Polymorphism paradigm which allow to us have method with the same
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


# It is here to show that attributes are variable which can be accessed throuh
# instances of class
my_pet1 = Mammals('Oskar')
my_pet2 = Fish('Goldy', 0.5)
my_pet3 = Reptiles('Tom', 4)


print(f"My second pet's name is {my_pet1.name}. He's {my_pet1.age} years old.")
print(f"My second pet's name is {my_pet2.name}. He's {my_pet2.age} years old.")
print(f"My third pet's name is {my_pet3.name}. He's {my_pet3.age} years old.")
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
