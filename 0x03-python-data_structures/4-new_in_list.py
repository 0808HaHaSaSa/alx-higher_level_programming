#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    a = len(my_list)
    i = 0
    if idx < 0:
        return my_list
    elif idx >= a:
        return my_list
    else:
        my_list2=my_list.copy()
        my_list2[idx] = element
        return my_list2
