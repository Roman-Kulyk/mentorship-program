class Animal:
    def eat(self):
        print('I can eat!')

    
    def sleep(self):
        print('I can sleep')


class Dog(Animal):
    def bark(self):
        print('I can bark! Woof woof!!')


dog1 = Dog()


dog1.eat()
dog1.sleep()
dog1.bark()