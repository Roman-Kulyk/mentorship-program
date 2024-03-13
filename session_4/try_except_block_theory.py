# The try block lets you test a block of code for errors.
# The except block lets you handle the error.
# The else block lets you execute code when there is no error
# The finally block lets you execute code, regardless of the result of the try-
# and except blocks.

# Exception Handling
# print(x)# Without the try block, the program will crash and raise an error.

try:
    # The try block will generate an exception, because x is not defined.
    print(x)
except:
    print('An exception occured.')
    # Since the try block raises an error, the except block will be executed.
print()

# Many Exception
# You can define as many exception blocks as you want, e.g. if you want to
# execute  a special block of code for a special kinf of error.
try:
    print(x)
except NameError:
    print('Variable x is not defined.')
except:
    print('Something else is wrong.')
print()
# Else 
# You can use the else keyword to define a block of code to be executed if no
# errors were raised.
# In this example, the try block does not generate any error.
try:
    print('Hello!')
except:
    print('Something wetn wrong!')
else:
    print('Nothing went wrong!')
print()
# Finally
# The finally block, if specified, will be executed regardless if the try block
# raises an error or not.
try:
    print(x)
except:
    print('Something went wrong!')
finally:
    print("The 'try except' is finished!")
print()
# This can be useful to close and clean up resources.
try:
    f = open('demofile.txt')
    try:
        f.write('Lorum Ipsum')
    except:
        print('Something went wront when writing to the file!')
# The program can continue, without leaving the file object open.
    finally:
        f.close()
except:
    print('Something went wrong when opening the file.')
print()
