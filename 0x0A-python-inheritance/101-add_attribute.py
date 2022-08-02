#!/usr/bin/python3
"""
=============================
Module with a method add_attribute()
=============================
"""


def add_attribute(obj, name, value):
    """Method that add attribute"""
    if hasattr(obj, '__dict__') or name in getattr(obj, '__slots__', {}):
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")
