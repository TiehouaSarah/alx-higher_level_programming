def safe_print_list(my_list=[], x=0):
    y = 0
    try:
        while (y < x):
            print(my_list[y], end="")
            y = y + 1
        else:
            print()
    except:
        print("")
    return y
