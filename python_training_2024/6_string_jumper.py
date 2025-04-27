"""
Welcome to the part 2 of For Loops in Python. In this question, we'll learn to print 
characters of a string at even indices.
You are given a string str, you need to print its characters at even indices(index starts at 0).
Note: Please go through the range function to understand how to jump 2 steps.
"""


def string_jumper(text):
    for i in range(len(text)):
        if i % 2 == 0:
            print(text[i], end=" ")


string_jumper("DoctorPhenomenal")
print()
string_jumper("Geeks")
