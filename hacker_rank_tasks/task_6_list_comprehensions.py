if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    list_1 = range(0, x + 1)
    list_2 = range(0, y + 1)
    list_3 = range(0, z + 1)

    print([[x,y,z] for x in list_1 for y in list_2 
           for z in list_3 if sum([x, y, z]) != n])


