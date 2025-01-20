# In Pythons, the Assertion is a boolean expression that checks whether the
# the condition returns true of false. If the condition is true then, the
# further progrma will be executed i.e. the Assertion will not affect the
# program and it moves to the next line of code of the program. But, if the
# condition is false, then it will throw the Assertion Error and stop the
# execution of the program.

# Python assert keyword without error message
# initializing numbers
a = 4
b = 0
# using assert to check for 0
print('The value of a / b is: ')
assert b != 0
print(a / b)

# # Python assert keyword with error message
# # initializing numbers
# a = 4
# b = 0
# # using assert to check for 0
# # print('The value of a / b is: ')
# assert b != 0, 'Zero Division Error'
# print(a / b)
# # Assert Inside a Function
# # Function to calculate the area of a rectangle


# def calculate_rectangle_area(length, width):
#     # Assertion to check that the length and width are positive
#     assert length > 0 and width > 0, "Length and width" + \
#         "must be positive"
#     # Calculation of the area
#     area = length * width
#     # Return statement
#     return area


# # Calling the function with positive inputs
# area1 = calculate_rectangle_area(5, 8)
# print('Area  of rectangle with length 5 and width 8 is', area1)


# # Calling the function with negative inputs
# area2 = calculate_rectangle_area(-5, 8)
# print('Area of rectangle with length -5 and width 8 is', area2)

# # Assert with boolean Condition
# # Initializing variables
# # In this example, the assert statement checks whether the boolean condition
# # x < y is true. If the assertion fails, it raises an AssetionError. It the
# # assertion passes, the program continues and prints the values of x and y.
# x = 10
# y = 20
# # Asserting a boolean condition
# assert x < y
# # Printing the values of x and y
# print('x =', x)
# print('y =', y)

# # Assert Type of Variable in Python
# # In this example, the assert statements check the types of the variables a
# # and b are str and int, respectivelyl. If any of the assertions fail, it
# # raises an AssertionError. If both assertions pass, the program continues
# # and prints the values of a and b.
# # Initializing variables
# a = 'Hello'
# b = 42
# # Asserting the type of a variable
# assert type(a) == str
# assert type(b) == int
# # Printing the values of a and b
# print('a =', a)
# print('b =', b)

# # Asserting dictionary values
# # In this example, the assert statements check whether the values with keys
# # 'apple', 'banana', and 'cherry' in the dictionary my_dict 1, 2, and 3,
# # respectively. If any of the asserions fail, it raises an AssertionError. If
# # all assertions pass, the program continues and prints the contents of the
# # dictionary.
# # Initializing a dictionary
# my_dict = {'apple': 1, 'banana': 2, 'cherry': 3}

# # Asserting the contents of the dictionary
# assert my_dict['apple'] == 1
# assert my_dict['banana'] == 2
# assert my_dict['cherry'] == 3
# # Printing the dictionary
# print('My dictionary contains the following key-value pairs:', my_dict)
# Practical Application
# Initializing list of foods temperatures
# batch = [40, 26, 39, 30, 25, 21]

# # Initializing cut temperature
# cut = 26

# # using assert to check for temperature greater tnan cut
# for i in batch:
#     assert i >= 26, 'Batch is Rejected'
#     print(str(i) + ' is OK')