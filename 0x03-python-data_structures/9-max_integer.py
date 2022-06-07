#!/usr/bin/python3
def max_integer(my_list=[]):
    a = len(my_list)
    if a == 0:
        return None
    else:
        i = 1
        b = my_list[0]
        while i < a:
            if b < my_list[i]:
                b = my_list[i]
            i = i + 1
        return b
