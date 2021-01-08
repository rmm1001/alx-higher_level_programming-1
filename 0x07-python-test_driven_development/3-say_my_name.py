#!/usr/bin/python3
"""
This module defines `say_my_name`

The function prints the full name using first_name and last_name
"""


def say_my_name(first_name, last_name=""):

    if not isinstance(first_name, str):
        raise TypeError('first_name must be a string')
    elif not isinstance(last_name, str):
        raise TypeError('last_name must be a string')

    print('My name is {} {}'.format(first_name, last_name))
