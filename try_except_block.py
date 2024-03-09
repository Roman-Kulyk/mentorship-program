short_list = [1, 2, 3]
position = 5
try:
    short_list[position]
except:
    print('Need a position between 0 and', len(short_list)-1, 'but got',
          position)

try:
    print(5/0)
except ZeroDivisionError:
    print('You can\'t divide by zero!')


predators = ['tiger', 'wolf', 'bear']
while True:
    value = input('Position [q to quit]?')
    if value == 'q':
        break
    try:
        position = int(value)
        print(predators[position])
    except IndexError as err:
        print('Bad index:', position)
    except Exception as other:
        print('Something else broke:', other)
print()


def divide(x, y):
    # This block will test the excepted error to occur
    try:
        result = x/y
    # Optional block, handling of exception (if required)
    except ZeroDivisionError:
        print("Division by zero!")
    # Execute  if no exeption
    else:
        print("Result is", result)
    # Some code ....(always executed)
    finally:
        print("End of the calculation.")


divide(2, 1)
divide(2, 0)
