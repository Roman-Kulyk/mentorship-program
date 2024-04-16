"""The @classmethod decorator is a built-in function decorator that is an
expression that gets evaluated after your function is definded. The results
of that evaluation shadows your function definition. A class method receives
the class as an implicit first argument, just like an instance method receives
the instance.
-A class method is a method that is bound to the class and not the object of
the class.
-They have the access to the state of the class as it takes a class parameter
that points to the class and not the object instance.
-It can modify a class state that would apply across all the instances of the
class. For example, it can modify a class variable that will be applicable to
all the instances.

A static method does not receive an implicit first argument. A static mehod is
also a method that is bound to the class and not the object of the class. This
method can't access or modify the class state. It is present in a class because
it makes sense for the method to be present in class."""


from datetime import date


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def fromBirthYear(cls, name, birtYear):
        return cls(name, date.today().year - birtYear)

    # @classmethod
    # def myClassMethod1(cls):
    #     pass

    # @classmethod
    # def myClassMethod2(cls):
    #     pass

    def display(self):
        print(self.name + "'s age is: " + str(self.age))

    @staticmethod
    def fromFatherAge(name, fatherAge, fatherPersonAgeDiff):
        return Person(name, date.today().year - fatherAge + fatherPersonAgeDiff)

    # @classmethod
    # def myStaticMethod1(cls):
    #     pass

    # @classmethod
    # def myStaticMethod2(cls):
    #     pass


class Man(Person):
    sex = 'Male'


man1 = Man.fromFatherAge('John', 1965, 20)  # It is staticmethod
print(isinstance(man1, Man))
man1.display()
print(type(man1))
print()

man2 = Man.fromBirthYear('John', 1985)  # It is classmethod
print(isinstance(man2, Man))
man2.display()
print(type(man2))
print()

man2 = Man.fromFatherAge('John', 1985, 25)  # It is staticmethod
print(isinstance(man2, Man))
man2.display()
print(type(man2))
print()

man3 = Man('Roman', 1980)  # It is classmethod
print(isinstance(man3, Man))
man3.display()
print(type(man3))
