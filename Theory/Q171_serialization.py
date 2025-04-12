# https://www.linkedin.com/pulse/serialization-deserialization-aka-pickling-unpickling-victor-bekee#:~:text=Serialization%20is%20the%20process%20of,the%20functionality%20to%20perform%20serialization.
"""
Serialization and deserialization, also known as pickling and unpickling in Python,
are processes used to convert complex data structures, such as objects or data
collections, into a format that can be easily stored or transmitted and then
reconstructed later. It allows you to convert objects or data into a serialized form,
which can be saved to a file, sent over a network, or stored in a database.

Serialization (Pickling):
Serialization is the process of converting a Python object into a byte stream or
a string representation that can be easily stored or transmitted. The serialized
form preserves the object's structure and internal data. In Python, the built-in
pickle module provides the functionality to perform serialization. The process of
serialization is often referred to as "pickling" because of the module's name.
"""

import pickle
# Picle the data
data = {'name':'John', 'age':30, 'city':'New York'}

with open('data.pickle', 'wb') as file:
    pickle.dump('data.pickle', file)

"""
Deserialization is the process of reconstructing a serialized object from its serialized
form. It involves reading the serialized data from a file or a network stream and
converting it back into a Python object. In Python, the pickle module provides the
pickle.load() function to perform deserialization, often called "unpickling."
"""
import pickle
# Unpicle the data
with open('data.pickle', 'rb') as file:
    data = pickle.load(file)

print(data)
# Output: {'name': 'John', 'age': 30, 'city': 'New York'}
