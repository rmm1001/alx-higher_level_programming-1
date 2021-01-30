#!/usr/bin/python3
""" pascal triangle"""


def pascal_triangle(n):
    """print pascal"""
    pascal = []
    for i in range(0, n, -1):
        inner = []
        for j in range(n - i):


[1]
[1,1]
[1,2,1]
[1,3,3,1]
[1,4,6,4,1]