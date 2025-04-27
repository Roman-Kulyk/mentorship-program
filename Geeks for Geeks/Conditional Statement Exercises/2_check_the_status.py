"""
Given two integer variables a and b, and a boolean variable flag. 
The task is to check the status and return accordingly.
Return True for the following cases:
Either a or b (not both) is non-negative and the flag is false.
Both a and b are negative and the flag is true.
Otherwise, return False.
"""


def check_the_status(a, b, flag):
    if (a >= 0 or b >= 0 ) and flag is False:
        result = True
    elif (a < 0 and b < 0) and flag is True:
        result = True
    else:
        result = False
    print(result)
    return result
    

check_the_status(1, -1, False)
check_the_status(-182, -9121, True)
check_the_status(5, 3, True)
