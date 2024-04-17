"""Serialization is the process of converting a Python object into a byte stream
or a string representation that can be easily stored or transmitted.
Deserialization is the process of reconstructing a serialized object from
its serialized form. It involves reading the serialized data from a file or a
network stream and converting  it back into a Python object.
"""
# Pickle module is the standard Python library for serializing and deserializing
# Python objects. It is a binary protocol, which means the resulting byte stream
# is not human-readable.
import pickle
data = {'name': 'John', 'age': 30, 'city': 'New York'}

with open('data.pickle', 'wb') as file:
    pickle.dump(data, file)
    print('Pickling completed...')

with open('data.pickle', 'rb') as file:
    data = pickle.load(file)
    print('Unpickling completed...')
    print(data)
print()
# JSON module - it is a newly created module. It allows to work with standard
# JSON files. JSON is a widely used format for data exchange and it is very
# convenient. It is human-readable and language-independent, and it's lighter
# than XML. It is a good choice if we want to interoperability among different
# languages
import json
# JSON string
students = '{"id":"9607", "name":"Sunny", "department":"Computer"}'
# Convert stritn to Python dict
student_dict = json.loads(students)
print(student_dict)

print(student_dict['name'])
print('Deserialization Completed')
print()

data = {"id": "877",
        "name": "Mayur",
        "department": "Comp"}
# Serializing json
json_object = json.dumps(data)
print(json_object)
print('Serialization Completed.')

# YAML 
# It is a human-friendly data serialization format for all programming
# languages.

# JOBLIB
# The joblib package provides dump and load functions for serializing Python
# objects, with particular optimizations for large numpy arrays.
