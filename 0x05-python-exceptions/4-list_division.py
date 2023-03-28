#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = [0] * list_length
    list_length_2 = 0
    next_length = 0
    try:
        while (list_length_2 < list_length):
            for index, item in enumerate(my_list_1):
                next_length = next_length + 1
                if isinstance(item, int) or isinstance(item, float):
                    if len(my_list_2) > index:
                        denominateur = my_list_2[index]
                        if isinstance(denominateur, int) or isinstance(denominateur, float):
                            if denominateur != 0:
                                quotient = item // denominateur
                                new_list[list_length_2] = float(quotient)
                            else:
                                new_list[list_length_2] = 0
                                print("division by 0")
                        else:
                            new_list[list_length_2] = 0
                            print("wrong type")
                else:
                    new_list[list_length_2] = 0
                list_length_2 = list_length_2 + 1
    except IndexError:
        new_list[list_length_2 - 1] = 0
        print("out of range")
    finally:
        return new_list
