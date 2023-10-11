#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    keys = list(a_dictionary.keys())
    keys.sort()
    for sorted_key in keys:
        print("{}: {}".format(sorted_key, a_dictionary[sorted_key]))
