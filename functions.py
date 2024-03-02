# Functions in Python is a block of statements that return the specific task.
# A simple Python function
def my_function():
    print("Hello from GL Ukraine!")

# Driver code to call a function
my_function()

def mul(num1: int, num2: int) -> int:
    """Multiply two numbers"""
    num3 = num1 * num2
    return num3


# Driver code
num1, num2 = 3, 6
ans = mul(num1, num2)
print(f"The multiplication of {num1} and {num2} results {ans}.")


# A simple Python function to check 
# whether x is even or odd
def evenOdd(x):
    if (x % 2 == 0):
        print("even")
    else:
        print("odd")
# Driver code to call the function
evenOdd(18)
evenOdd(9)
print()
