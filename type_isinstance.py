#two options

#type(object) -> the object's type
numbers_list = [2,3]
print(type(numbers_list))

numbers_dict = { 2:'two',3:'three'}
print(type(numbers_dict))

class Foo:
    a = 0

foo = Foo()
print(type(foo))

#type(name, bases, dict, **kwds) -> a new type,
o1 = type('X',(object,), dict(a='Foo', b=12))
print(type(o1))
print(vars(o1))

class test:
    a = 'Foo'
    b = 12

o2 = type('Y', (test,), dict(a='Foo', b=12))
print(type(o2))
print(vars(o2))
print()
#isinstance returns whether an object is an instance of a class or of a subclass thereof.
class Foo:
    a = 5

fooInstance = Foo()

print(isinstance(fooInstance, Foo))
print(isinstance(fooInstance, (list,tuple)))
print(isinstance(fooInstance, (list, tuple, Foo)))

numbers = [3,4,5]
result = isinstance(numbers, list)
print(numbers, 'instance of list?', result)

result = isinstance(numbers,dict)
print(numbers,'instance of dict?',result)

result = isinstance(numbers,(dict,list))
print(numbers,'instance of dict or list?',result)

number = 7
result = isinstance(number, list)
print(number,'isinstance of lists?', result)

result = isinstance(number, int)
print(number, 'isinstance of int?', result)

#main difference is that isinstance returns boolean value, and type returns type of object