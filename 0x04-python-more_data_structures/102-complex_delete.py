#!/usr/bin/python3
def complex_delete(my_dict, value):    
    return {k: v for k, v in my_dict.items() if value not in v }
