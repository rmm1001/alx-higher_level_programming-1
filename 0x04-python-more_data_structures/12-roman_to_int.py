#!/usr/bin/python3
def roman_to_int(roman_string: str):
    if not roman_string:
        return
    data = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    numbers = [data[x] for x in reversed(roman_string)]
    rep = numbers.pop(0)

    for x in numbers:
        #print(rep, x, x >= rep)
        if x >= rep:
            rep += x
        else:
            rep -= x
    return rep

roman_number = "X"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "MDCCLXXVI"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "IX"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "LXXXVII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "DCCVII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))
