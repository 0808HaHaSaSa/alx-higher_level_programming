#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    a = len(my_list)
    i = a - 1
    while i >= 0:
         print("{}".format(my_list[i]))
         i = i - 1
