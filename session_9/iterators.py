for element in [1, 2, 3]:
    print(element)
for element in (1, 2, 3):
    print(element)
for key in {'one': 1, 'two': 2}:
    print(key)
for char in '123':
    print(char)
for line in open('myfile.txt'):
    print(line, end='')

"""
This style of access is clear, consice, and convinient. The use of iterators
pervades and unifies Python. Behind the scenes, the for statement calls
iter() on the container object. The function returns an iterator object that
defines method __next__() which accesses elements in the container one at a
time. When there are no more elements, __next__() raises a StopIteration
exception which tells the for loop to terminate.
"""


class Reverse:
    """Iterator for looping over a sequence backwards."""
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]


rev = Reverse('spam')
iter(rev)
for char in rev:
    print(char)
