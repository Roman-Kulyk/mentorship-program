"""
This tool returns successive  length permutations of elements in an iterable.

If  is not specified or is None, then  defaults to the length of the iterable, and all possible full length permutations are generated.

Permutations are printed in a lexicographic sorted order. So, if the input iterable is sorted, the permutation tuples will be produced in a sorted order.
Task
You are given a string S.
Your task is to print all possible permutations of size  of the string in lexicographic sorted order.
Input Format
A single line containing the space separated string  and the integer value .
Constraints
0<k<=len(S)
The string contains only UPPERCASE characters.
Output Format
Print the permutations of the string  on separate lines.
Sample Input
HACK 2
Sample Output
AC
AH
AK
CA
CH
CK
HA
HC
HK
KA
KC
KH
Explanation
All possible size 2 permutations of the string "HACK" are printed in lexicographic sorted order.
"""
# Enter your code here. Read input from STDIN. Print output to STDOUT
