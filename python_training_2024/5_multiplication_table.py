"""
Writing for loop in Python is a tad different from C++ and Java counterparts. 
In this question, we'll learn to print table by using the for loop.
You are given a number N, you need to print its multiplication table.
"""


def multiplication_table(num):
    for i in range(10):
        print(i * num, end=" ")


multiplication_table(5)
print()
multiplication_table(6)
