"""newlist = [EXPRESSIN for ITEM in ITERABLE if CONDITION == True]"""

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
