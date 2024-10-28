# Enter your code here. Read input from STDIN. Print output to STDOUT

n = input(int())
t = map(int, input().split())
result = tuple(t)
print(hash(result))