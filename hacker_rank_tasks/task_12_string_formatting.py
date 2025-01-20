"""
Given an integer, n, print the following values for each integer i from 1 to n:
1. Decimal
2. Octal
3. Hexadecimal (capitalized)
4. Binary
Function Description
Complete the print_formatted function in the editor below.
print_formatted has the following parameters:
- int number: the maximum value to print
Prints
The four values must be printed on a single line in the order specified above for each i from 1 to number.
Each value should be space-padded to match the width of the binary value of  and the values should be separated by
a single space.
Input Format
A single integer denoting .
Constraints
1 <= n <= 99
"""


def print_formatted(number):
    # your code goes here
    b_max_len = len(bin(n))-2  # to compensate the deletion of prefix in oct, hex, and bin
    
    for i in range(1, n + 1):
        print(str((i)).rjust(b_max_len), 
             (oct(i)[2:]).rjust(b_max_len),  # sliced to remove prefix
             (hex(i)[2:].upper()).rjust(b_max_len),  # sliced to remove prefix
             (bin(i)[2:]).rjust(b_max_len))  # sliced to remove prefix


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
