"""
Given a natural number n, the task is to write a Python program to first find the sum
of first n natural numbers and then print each step as a pattern.
"""
def print_nat_num_sum(n):
    for j in range(1, n + 1):
        a = []
        for i in range(1, j+1):
            print(i, sep=" ", end=" ")
            if (i < j):
                print("+", sep=" ", end=" ")
            a.append(i)
        print("=", sum(a))

print_nat_num_sum(20)
