class IsNotTitleException(Exception):
    pass


try:
    rooms = ['Kitchen', 'study', 'Hall', 'Bathroom']
    for room in rooms:
        if room.title() != room:
            raise IsNotTitleException('Fault!')

except IsNotTitleException as exc:
    print(exc)


# The raise statement allows the programmer to force a specified exception to
# occur
# raise NameError('HiThere')


# try:
#     raise NameError('HiThere')
# except NameError:
#     print('An exception flew by!')
#     raise

# Raise an exception
# To throw(or raise) and exception, use the raise keyword.
# Raise an error and stop the program if x is lower tnan 0.
# x = -1

# if x < 0:
#     raise Exception('Sorry, no numbers below zero.')
# The raise keyword is used to raise an exception.
# You can define what kind of error to raise, and the text to print to the user.
# Raise a TypeError if x is not an integer.
x = 'hello'
if not type(x) is int:
    raise TypeError('Only integers are alloved')