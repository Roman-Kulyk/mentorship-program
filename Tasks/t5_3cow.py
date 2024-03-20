class Cow:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(self.name + " is now eating grass!")

    def drink(self):
        print(self.name + " is now drinking water!")

    def produce_milk(self):
        print(f'{self.name} produces a lot of milk.')

    def speak(self):
        print(f'{self.name} can speak but only Mo-o-o-o!')


Romashka = Cow('Romashka', 5)
Romashka.eat()
Romashka.drink()
Romashka.produce_milk()
Romashka.speak()
