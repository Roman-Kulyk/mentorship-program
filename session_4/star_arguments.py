# The special syntax *args in function definition in Python is used to pass a
# variable number of arguments to a function. It is used to pass a non-keyword,
# variable-length argument list.
def myFun(*argv):
    for arg in argv:
        print(arg)


myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')


def print_days(*args):
    print('Get ready:', args)


print_days('Wednesday', 'Thursday', 'Friday', 'Weekend...')
print()


def print_travel(required1, required2, *args):
    print('For train travel is required:', required1)
    print('For train travel is required too:', required2)
    print('All the rest:', args)


print_travel('return ticket', 'train', 'carriage', 'seat', 'luggage rack')

# The special syntax **kwargs in function definition in Python is used to pass
# a keyworded, variable-length argument list. We use the name **kwargs with the
# double star. The reason is that the double star allows us to pass through
# keyword arguments(and any number of them).


def myFun(**kwargs):
    for key, value in kwargs.items():
        print('%s == %s' % (key, value))


myFun(first='Geeks', mid='for', last='Geeks')
print()


def print_character(**kwargs):
    print('Person\'s characteristics:', kwargs)


print_character(emotions='cheerful', sense='happy', look='slim')
