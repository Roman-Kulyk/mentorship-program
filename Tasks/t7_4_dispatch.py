from multipledispatch import dispatch


class Mammals:
    """
    This is a class that defines Mammals.

    Attributes
    age:int
        age of an animal
    weight:int
        weight of an animal

    Methods

    move(self)
        Prints how the animal moves.
    reproduce(self)
        Prints how the animal reproduces.
    breathe(self)
        Prints how the animal breathes.
    eat(self)
        Prints what the animal eats.
    """
    def __init__(self: object, name: str, age: int) -> object:
        """
        Constructs all the necessary attributes for the animal object.

        Parameters
        name:str
            age of an animal
        age:int
            age of an animal
        """
        self.name = name
        self.age = age

    def move(self: object) -> None:
        """This is the method to prints how animal moves."""
        print('I can run!!!')

    def reproduce(self: object) -> None:
        """This is the method to prints how animal reproduces."""
        print('We give birth to live babies.')

    def breathe(self: object) -> None:
        """This is the method to prints how animal breathes."""
        print("I can breathe only air though my lungs!")

    @dispatch(int)
    def eat(self: object, a: int) -> int:  # is it correct to have int here
        """This is the method to prints what animal eats."""
        print(f"I'd like to eat {a} candies.")

    @dispatch(float)
    def eat(self: object, a: float) -> float:
        """This is the method to prints what animal eats."""
        print(f"I'd like to eat {a} kilos of grass!")

    @dispatch(str)
    def eat(self: object, a: str) -> str:
        """This is the method to prints what animal eats."""
        print(f"I'd like to eat {a}!")


my_pet1 = Mammals('Oskar', 2)
print(f"My second pet's name is {my_pet1.name}. He's {my_pet1.age} years old.")
my_pet1.breathe()
my_pet1.eat(3)
my_pet1.eat(3.5)
my_pet1.eat('grass')
my_pet1.move()
my_pet1.reproduce()
