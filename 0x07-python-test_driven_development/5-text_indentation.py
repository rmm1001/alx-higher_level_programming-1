#!/usr/bin/python3
"""
This module defines `text_indentation`

The function prints a text with 2 new lines after each of
these characters: ., ? and :
"""


def text_indentation(text):

    for l in '.:':
        text = text.replace(l, '\n')

    for line in text.splitlines():
        print(line.strip())
