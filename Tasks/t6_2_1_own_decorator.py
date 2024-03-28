def smart_add_to_list(func):
    def inner(*args):
        num_list_even = []
        num_list_odd = []
        for i in args:
            if i % 2 == 0:
                num_list_even.append(i)
            else:
                num_list_odd.append(i)
        if num_list_even != []:
            print('I got decorated even numbers list:', num_list_even)
        else:
            print("Whoops, where is an empty list!")

        if num_list_odd != []:
            print('I got decorated odd numbers list:', num_list_odd)
        else:
            print("Whoops, where is an empty list!")

        return func(*args)
    return inner


@smart_add_to_list
def add_to_list(*args):
    num_list = []
    num_list.extend(args)
    print('It is a number list from ordinary function:', num_list)


add_to_list(2, 5, 6, 8, 9)


print()
add_to_list(1, 3, 5, 7)
