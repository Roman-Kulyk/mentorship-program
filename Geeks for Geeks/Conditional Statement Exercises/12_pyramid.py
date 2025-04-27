"""
Pyramid patterns are sequences of characters or numbers arranged in a way
that resembles a pyramid, with each level having one more element than the
level above.
"""


def full_pyramid(n):
    for i in range(1, n +1):
        # print leading spaces
        for j in range(n -i):
            print(" ", end="")

        for k in range(1, 2*i):
            print("*", end="")
        print()

full_pyramid(5)
