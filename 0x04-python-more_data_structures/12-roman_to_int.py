#!/usr/bin/python3
def roman_to_int(roman_string:str):
    if not roman_string:
        return
    rep = 0
    data = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    numbers = [data[x] for x in roman_string]
    print(numbers)
    for x in range(len(data)):

roman_number = "LXXXVII"
roman_to_int(roman_number)
#print("{} = {}".format(roman_number, roman_to_int(roman_number)))