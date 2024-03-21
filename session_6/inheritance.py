"""Generally speaking, inheritance is the mechanism of deriving new classes
from existing ones. In most class-based object-oriented languages, an object
created through inheritance(a 'child object') acquires all of the properties
and behaviours of the parent object.
"""


class Robot:

    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print("Hi, I am " + self.name)


class PhysicianRobot(Robot):
    pass


x = Robot('Marvin')
y = PhysicianRobot('James')
# As the class PhysicianRobot is a subclass of Robot, it inherits in this case,
# both methods __init__ and say_hi. We can apply the say_hi method to the
# PhysicianRobot object y.

print(x, type(x))
print(y, type(y))

y.say_hi()
"""Diffeerence between type and isinstance
The difference can be seen it the following code. We see that isinstance
returns True if we compare an object either with the class it belongs to or
with the superclass. Whereas the equality operator only returns True, if we
compare an objec with its own class.
"""
print(isinstance(x, Robot), isinstance(y, Robot))
print(isinstance(x, PhysicianRobot))
print(isinstance(y, PhysicianRobot))


print(type(y) == Robot, type(y) == PhysicianRobot)
print(type(x) == Robot, type(x) == PhysicianRobot)
# Object type compriaons should always use isinstance() instead of comparing
# types directly.
