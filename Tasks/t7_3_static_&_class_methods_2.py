class MyClass:
    class_variable = 0  # Is a class-level attribute

    def __init__(self, instance_variable):  # Instance -level attribute
        self.instance_variable = instance_variable

    @classmethod
    def class_method(cls, x):
        """Class_methods modifies the class level attribute"""
        cls.class_variable += x

    @staticmethod
    def static_method(x):
        """Static methods simply returns its argument."""
        result = x
        return result


obj1 = MyClass(5)
print(f'MyClass variable: {MyClass.class_variable}')
print(f'My object instance variable: {obj1.instance_variable}')
print()

MyClass.class_method(1)
print(f'MyClass variable: {MyClass.class_variable}')
print(f'My object instance variable: {obj1.instance_variable}')
print()

obj1.class_method(2)
print(f'MyClass variable: {MyClass.class_variable}')
print(f'My object instance variable: {obj1.instance_variable}')
print()

obj2 = MyClass(4)
# obj2.static_method(3)
print(f'MyClass variable: {MyClass.class_variable}')
print(f'My object instance variable: {obj2.instance_variable}')
print(f'My object.static_method: {obj2.static_method(3)}')
print()

print(f'MyClass variable: {MyClass.class_variable}')
print(f'My object instance variable: {obj2.instance_variable}')
print(f'My object.static_method: {obj2.static_method(4)}')
print("The End")
