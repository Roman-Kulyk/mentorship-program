"""
You are given a string str, you need to return True if  the words "cat" and "hat"
appear same number of times in str, otherwise return False.
Note: str contains only lowercase English alphabets.
"""


def cat_and_hat(phrase):
    x = phrase.count('cat')
    # print(x)
    y = phrase.count('hat')
    # print(y)
    if (x == y) and x != 0:
        result = True
    else:
        result = False
    print(result)
    return result


cat_and_hat("catinahat")
cat_and_hat("bazingaa")
