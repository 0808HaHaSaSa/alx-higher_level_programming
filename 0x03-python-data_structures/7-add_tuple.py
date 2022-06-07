#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a = len(tuple_a)
    b = len(tuple_b)
    i = 0
    if a >= 2 and b >= 2:
        c = tuple_a[0] + tuple_b[0]
        d = tuple_a[1] + tuple_b[1]
        return c, d
    elif a == 1:
        c = tuple_a[0] + tuple_b[0]
        d = 0 + tuple_b[1]
        return c, d
    elif b == 1:
        c = tuple_a[0] + tuple_b[0]
        d = 0 + tuple_a[1]
        return c, d
    elif b == 1 and a == 1:
        c = tuple_a[0] + tuple_b[0]
        d = 0 + 0
        return c, d
    elif b == 0:
        c = tuple_a[0] + 0
        d = 0 + tuple_a[1]
        return c, d
    elif a == 0:
        c = tuple_b[0] + 0
        d = 0 + tuple_b[1]
        return c, d
    elif a == 0 and b == 0:
        c = 0 + 0
        d = 0 + 0
        return c, d
    else:
        c = tuple_a[0] + tuple_b[0]
        d = tuple_a[1] + tuple_b[1]
        return c, d
