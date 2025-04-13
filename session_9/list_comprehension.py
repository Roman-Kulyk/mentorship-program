"""List comprehension provides a concise way to create a list. Common applications
are to make new lists where each element is the result of some operations
applied to each member of another sequence or iterable, or to create a
subsequence of those elements that satisfy a certain condition.

newlist = [EXPRESSION for ITEM in ITERABLE if CONDITION == True]

A list comprehension consist of brackets containing an expression followed by a
for clause, then zero or more for or if clause. The result will be a new list
resulting from evaluating the expression in the context of the for and if
clauses which follow it.
"""

fruits = ["apple", "banana", "kiwi", "mango"]
newlist = []
for x in fruits:
    if "a" in x:
        newlist.append(x)
print(f"This is a newlist: {newlist}")

newlist_1 = [x for x in fruits if "a" in x]
print(f"This is a newlist_1: {newlist_1}")

newlist_2 = [x for x in fruits if x != 'apple']
print(f"This is a newlist_2: {newlist_2}")

newlist_3 = [x for x in fruits]
print(f"This is a newlist_3: {newlist_3}")

newlist_4 = [x for x in range(10)]
print(f"This is a newlist_4: {newlist_4}")

newlist_5 = [x for x in range(10) if x < 5]
print(f"This is a newlist_5: {newlist_5}")

newlist = [x.upper() for x in fruits]
print(f"This is a newlist: {newlist}")

newlist = ['hello' for x in fruits]
print(f"This is a newlist_: {newlist}")

newlist = [x if x != 'banana' else 'orange' for x in fruits]
print(f"This is a newlist: {newlist}")

""""Some simple generators can be coded succinctly as expressions using a syntax
similar to list comprehensions but with parentheses instead of square brackets.
These expressions are designed for situations where the generator is used right
away by an enclosing function. Generator expressions are more compact but less
versatile than full generator definitions and tend to be more memory friendly
than equivaent list comprehensions."""

a = sum(i*i for i in range(10))
print(a)

xvec = [10, 20, 30]
yvec = [7, 5, 3]
b = sum(x*y for x, y in zip(xvec, yvec))
print(b)

data = 'golf'
c = list(data[i] for i in range(len(data)-1, -1, -1))
print(c)
