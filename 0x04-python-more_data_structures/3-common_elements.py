#!/usr/bin/python3
def common_elements(set_1, set_2):
    a = len(set_1)
    b = len(set_2)
    i = 0
    m =[]
    while i < a:
        j = 0
        l = 0
        while j < b:
            if set_1[i] == set_2[j]:
                l = l + 1
            j = j + 1
        if l != 0 :
            m + set_1[i]
        i = i + 1
    return m
