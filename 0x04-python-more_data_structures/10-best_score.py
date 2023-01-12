#!/usr/bin/python3
def best_score(a_dictionary):

    if a_dictionary is None or a_dictionary == 0:
        return None
    best = max(a_dictionary.values())
    for key in a_dictionary.keys():
        if a_dictionary[key] == best:
            return key
