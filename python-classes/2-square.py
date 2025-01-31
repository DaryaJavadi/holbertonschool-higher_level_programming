#!/usr/bin/python3
"""This module defines a class named 'Square' with a private instance
attribute 'size'"""


class Square:
    """Defines a square by its 'size', ensuring it's an integer and non-negative"""
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
