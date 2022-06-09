#!/usr/bin/python3
def search_replace(my_list, search, replace):
    a = len(my_list)
    i = 0
    m = my_list.copy()
    while i < a:
        if m[i] == search:
            m[i] = replace
        i = i + 1
    return m
