"""
PEP498 introduced a new string formatting mechanism known as Literal String
Interpolation or more commonly as F-strings. The idea behind f-strings to make 
string interpolation simler.
A formatted string literal or f-string is a literal that is prefixed with 'f' or
'F'. These strings may contain replacement fields, which are expressions
delimited by curly braces{}. While other string literals always have a constant
value, formatted strings are really expressions evaluated at run time.
"""
name = 'David'
print(f'My name is {name}')


a = 12
b = 8
print(f'12 + 8 = {a + b}')


price = 250.67890
print(f'your account: {price:.3f}')


value = 4 * 20
# 1 option
print('The value is {value}.'.format(value = value))# it is format function
# 2 option
print('The value is {}.'.format(value))# it is simplest form of format function
# 3 option
print(f'The value is {value}.')# it is formatted string