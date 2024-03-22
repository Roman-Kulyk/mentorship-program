"""Decorators allow us to wrap another function in order to extend the behavior
of the wrapped function, without permanently modifyint it.
"""
def make_pretty(func):
    def inner():
        print('I got decorated')
        func()
    return inner


# def ordinary():
#     print('I am ordinary')


# decorated_func = make_pretty(ordinary)  # it creates a decorator function
# decorated_func()  # it calls a decorator function


@make_pretty
def ordinary():
    print('I am ordinary')


ordinary()
