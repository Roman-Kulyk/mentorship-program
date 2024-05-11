"""Generators are a simple and powerful tool for creating iterators. They are
written like regular functions but use the yield statement whenever they want
to return data. Each time next() is called on it, the generator resumes where
it left off (it remembers all the data values and which statement was last
executed).
"""


def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]


for char in reverse('golf'):
    print(char)

"""Anything that can be done with generators can also be done with class-based
iterators as described in the previous section. What makes generators compact
is that the __iter__() and __next__() methods are created automatically.
"""
