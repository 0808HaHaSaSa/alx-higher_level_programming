#!/usr/bin/python3
def uniq_add(my_list=[]):
    a = len(my_list)
    i = 0
    m = 0
    while i < a:
        l = 0
        j = 0
        while j < i:
            if my_list[i] == my_list[j]:
                l = l + 1
            j = j + 1
        if l == 0:
            m = m + my_list[i]
        i = i + 1
    return m
