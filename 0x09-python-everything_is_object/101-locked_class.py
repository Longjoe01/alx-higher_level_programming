#!/usr/bin/python3
""" Defines a class Lockedclass"""


class LockedClass:
    """Prevents the user from dynamically creating new instance
    attributes, except if the attribute is called first_name.
    """
    __slots__ = 'first_name'
