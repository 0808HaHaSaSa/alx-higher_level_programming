#!/usr/bin/python3
def pow(a, b):
if b == 0:
	return 1
elif b > 0:
	c = 1
	for i in range(0, b):
		c = c*a
	return c
else:
	c = 1
	for i in range(0, -b):
		c = c*a
	return 1/c
