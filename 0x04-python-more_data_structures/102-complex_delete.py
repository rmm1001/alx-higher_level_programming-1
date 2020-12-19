#!/usr/bin/python3
def complex_delete(my_dict, value):
    tmp = my_dict.copy()
    for k, v in tmp.items():
        if value in v:
            my_dict.pop(value)
    return my_dict
