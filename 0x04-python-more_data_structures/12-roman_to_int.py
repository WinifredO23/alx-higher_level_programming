#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or not isinstance(roman_string, str):
        return 0

    roman_num = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }

    res = 0
    pre_val = 0

    for c in reversed(roman_string):
        value = roman_num.get(c, 0)
        if value < pre_val:
            res -= value
        else:
            res += value
        pre_val = value

    return res
