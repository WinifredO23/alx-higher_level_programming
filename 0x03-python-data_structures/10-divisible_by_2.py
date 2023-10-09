#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    res = []
    for items in my_list:
        res.append(items % 2 == 0)
    return res
