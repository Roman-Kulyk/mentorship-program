class Animal:
    """
    This is a class that defines animals.

    Attributes
    age:int
        age of an animal
    weight:int
        weight of an animal

    Methods
    eat(self)
        Prints what the animal eats.
    """
    def __init__(self, age=50, weight=25):
        """
        Constructs all the necessary attributes for the animal object.

        Parameters
        age:int
            age of an animal
        weight:int
            weigh of an animal
        """
        self._age = age
        self._weight = weight

    def eat(self) -> None:
        """This method describe the most neccessary function of animals body"""
        print('I can eat.')

    @property
    def age(self) -> int:
        """This is a method to ..."""
        return self._age

    # @age.getter
    # def age(self):
    #     return self.age

    @age.setter
    def age(self: object, value: int):
        """
        This is a method to set the age value to the protected attribute for
        Animal class.
        """
        self._age = value

    @age.deleter
    def age(self) -> None:
        """
        This is a method to set default value for age attribute for
        animals.
        """
        self._age = 20

    @property
    def weight(self) -> int:
        """This is a method to ..."""
        return self._weight

    # @weight.getter
    # def weight(self):
    #     return self.weight

    @weight.setter
    def weight(self: object, value: int):
        """
        This is a method to set the weight value to the protected attribute
        for Animal class.
        """
        self._weight = value

    @weight.deleter
    def weight(self) -> int:
        """
        This is a method to set default value for weight attribute for
        animals.
        """
        self._weight = 5


cat = Animal(weight=45)
print(cat.age)
print(cat.weight)

cat.age = 5
cat.weight = 10

del cat.age
del cat.weight

print(cat.age)
print(cat.weight)
print(Animal.__doc__)
