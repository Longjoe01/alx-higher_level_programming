#!/usr/bin/python3

class Mylist(list):

    """ represents a mylist
    """

    def print_sorted(self):
        """prints a sorted list
        """
        sorted_list = sorted(self)
        print(sorted_list)
