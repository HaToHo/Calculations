#!/usr/bin/python
#Filename: subtraction.py
__author__ = 'hans'


def subInt(a, b):
    """
    Always converts a and b to int values before the subtraction is performed.
     If the value cannot be converted it is equal to 0.
    :param a: A value of any type
    :param b: A value of any type.
    :return: a-b
    """
    try:
        a = int(a)
    except ValueError:
        a = 0
    try:
        b = int(b)
    except ValueError:
        b = 0
    return a - b
