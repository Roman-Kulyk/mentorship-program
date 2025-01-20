"""Decorators are just employed to add certain layout patterns to a method
without affecting the structure of function. Typiclly, decorators are identified
before  the event they will be improving. We should first define a decorator's
function before using it. The function to which we will implement the decorator
function is then written, and the decorator function is simply positioned above
it. In this instance, the @ symbol comes preceding the decorator.
"""
import time


def time_dec(func):
    def inner(*args):
        start_time = time.time()
        result = func(*args)
        finish_time = time.time()
        elapsed_time_secs = finish_time - start_time
        print(f"The task took {elapsed_time_secs:.4f} seconds to complete.")
    return inner


@time_dec
def my_function():
    time.sleep(2)
    return 'Finished'


my_function()
