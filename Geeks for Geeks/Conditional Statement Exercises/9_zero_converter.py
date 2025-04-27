"""
You are given a number n. The number n can be negative or positive. If n is negative,
print numbers from n to 0 by adding 1 to n in the neg funcgtion. If positive , print
numbers from n-1 to 0 by subtracting 1 from n in the pos function.
You don't have to return anything, you just have to print array.
"""

# Option 1
# def pos(n):
#     for i in range(n,0,-1):
#         print(i-1, end=" ")

# def neg(n):
#     for i in range(n-1,0,1):
#         print(i+1, end=" ")


# Option 2
# def pos(n):
#     for i in range(n-1,-1,-1):
#         print(i, end=" ")

# def neg(n):
#     for i in range(n,1):
#         print(i, end=" ")


# Option 3
def pos( n ):
    for i in range ( 1, n + 1 ): 
        print( n - i, end = " " )
def neg( n ):
    for i in range ( 1 - n ): 
        print( n + i, end = " " )

pos(4)
print()
neg(-3)
