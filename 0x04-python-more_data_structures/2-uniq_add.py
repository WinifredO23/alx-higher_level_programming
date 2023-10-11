#!/usr/bin/python3
def uniq_add(my_list=[]):

    unique_integers = []
    total = 0

    for n in my_list:
        if n not in unique_integers:
            total += n
            unique_integers.append(n)
    return total
