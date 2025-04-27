"""
Given a number x, the task is to print the numbers from x to 0 in decreasing order in a single line.
"""

def print_in_decreasing(num):
    while num >= 0:
        print(num)
        num -= 1


print_in_decreasing(3)
