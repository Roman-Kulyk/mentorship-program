# # 1.Class without getter and setter
# class Celsius:
#     def __init__(self, temperature = 0):
#         self.temperature = temperature


#     def to_fahrenheit(self):
#         return(self.temperature * 1.8) + 32


# human = Celsius()  # it creates new heman object from Celsius class
# human.temperature = 37  # it sets temperature
# print(human.temperature)
# print(human.to_fahrenheit())

# print(human.__dict__)


# # 2.Using getter and setter
# class Celsius:
#     def __init__(self, temperature = 0):
#         self.set_temperature(temperature)

#     def to_fahrenheit(self)    :
#         return (self.get_temperature() * 1.8) + 32
#     # getter method
#     def get_temperature(self):
#         return self._temperature  # protected members

#     # setter method
#     def set_temperature(self, value):
#         if value < -273.15:
#             raise ValueError('Temperature below -273.15 is not possible.')
#         self._temperature = value


# human = Celsius(37)

# print(human.get_temperature())

# print(human.to_fahrenheit())

# human.set_temperature(-300)

# print(human.to_fahrenheit())


# # 3. Using class property
# class Celsius:
#     def __init__(self, termperature=0):
#         self.temperature = termperature

#     def to_fahrenheit(self):
#         return (self.temperature * 1.8) + 32

#     # getter method
#     def get_temperature(self):
#         print('Getting value...')
#         return self._temperature

#     # setter method
#     def set_temperature(self, value):
#         print('Setting value...')
#         if value < -273.15:
#             raise ValueError('Temperature below -273.15 is not possible')
#         self._temperature = value

#     # creating object of property class
#     temperature = property(get_temperature, set_temperature)


# human = Celsius(37)

# print(human.temperature)

# print(human.to_fahrenheit())

# human.temperature = -300


# 4. Using decorator @property
class Celsius:
    def __init__(self, temperature=0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    @property
    def temperature(self):
        print('Getting value...')
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        print('Setting value...')
        if value < -273.15:
            raise ValueError('Temperature below -273 is not possible')
        self._temperature = value


human = Celsius(37)

print(human.temperature)

print(human.to_fahrenheit())

coldest_thing = Celsius(-300)
