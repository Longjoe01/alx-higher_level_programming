#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):

    """
    removes a key in a dict
    """
    if a_dictionary is None:
        return None
    if key in a_dictionary:
        del a_dictionary[key]
    return a_dictionary
