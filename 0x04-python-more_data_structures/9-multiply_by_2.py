#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    temp_dictionary = dict(a_dictionary)
    for key, value in temp_dictionary.items():
        temp_dictionary[key] = value * 2
    return temp_dictionary
