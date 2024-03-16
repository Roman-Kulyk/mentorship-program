class Car():
    def __init__(self, model, types, doors, fuel, engine):
        self.model = model
        self.types = types
        self.doors = doors
        self.fuel = fuel
        self.engine = engine

    def get_descriptive_name(self):
        print(f'I am {self.model} {self.types} with {self.engine} {self.fuel}')

    def start_driving(self):
        print(f'{self.model} starts driving!')

    def start_braking(self):
        print(f'{self.model} starts breaking!')


the_car = Car('VW Golf', 'hatchback', 5, 'TDI', 1.9)
the_car.get_descriptive_name()
the_car.start_driving()


the_car2 = Car('Audi A6', 'sedan', 5, 'TD', 2.4)
the_car2.get_descriptive_name()
the_car2.start_braking()
