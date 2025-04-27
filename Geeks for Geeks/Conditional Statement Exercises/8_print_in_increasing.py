"""
Given a positive integer x, the task is to print the numbers from 1 to x in the order
as 1**2, 2**2, 3**2, 4**2, 5**2, ... (in increasing order).
"""


def print_in_increasing(num):
    i = 1
    while i ** 2 < num:
        print(i ** 2, end=" ")
        i += 1


print_in_increasing(10)
