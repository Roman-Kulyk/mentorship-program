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


try:
    raise NameError('HiThere')
except NameError:
    print('An exception flew by!')
    raise
