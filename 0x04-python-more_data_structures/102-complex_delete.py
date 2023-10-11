#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    l_keys = list(a_dictionary.keys())

    for value in l_keys:
        if value == a_dictionary.get(value):
            del a_dictionary[value]

    return (a_dictionary)
