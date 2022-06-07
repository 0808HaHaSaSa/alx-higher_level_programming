#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    a = len(my_list)
    if a == 0:
        return None
    else:
        nlist = my_list.copy()
        i = 0
        while i < a:
            if my_list[i] % 2 == 0:
                nlist[i] = True
            else:
                nlist[i] = False
            i = i + 1
        return nlist
