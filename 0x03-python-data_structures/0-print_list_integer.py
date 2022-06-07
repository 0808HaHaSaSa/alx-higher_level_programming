#!/usr/bin/python3
def print_list_integer(my_list=[]):
    a = len(my_list)
    i = 0
    while i < a:
         print("{:d}".format(my_list[i]))
         i = i + 1
