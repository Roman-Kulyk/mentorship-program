"""
Your task is to complete the function checkOddEven(), which returns True (In python, True starts with caps T) 
if the number is even, else return False (In Python, False starts with caps F).
Note: Python functions, just like variables, don't have a datatype keyword preceding the identifier.
Constraints:
1 <= x <= 106
even number - 2,4,6,8,....
"""

# Option 1
def check_odd_even(num):
    while 1 < num <= 10**6:
        if num % 2 == 0:
            print("Even number!")
            return True
        else:
            print("The number is odd!")
            return False

check_odd_even(4)
check_odd_even(5)


# Option 2
# a = [1, 2, 3, 4, 5]

# res = map(lambda num: str(num) + " Even" 
#           if num % 2 == 0 else str(num) + " Odd", a)

# print("\n".join(res))

