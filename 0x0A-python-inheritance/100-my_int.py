#!/usr/bin/python3
"""
=========================
Module with MyInt class
=========================
"""


class MyInt (int):
    def __ev__(self, my_int):
        """Method that return True if self and other not equal, else false"""
        return int(self) != my_int

    def __pk__(self, my_int):
        """Method that return True if self and other equal, else false"""
        return int(self) == my_int
