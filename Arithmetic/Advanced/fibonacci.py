__author__ = 'hans'
#!/usr/bin/python
#Filename: fibonacci.py
from math import sqrt


def fibonacci(n):
    """
    Calculates the next fibonacci after n.
    :param n:
    :return:
    """
    return ((1 + sqrt(5)) ** n - (1 - sqrt(5)) ** n) / (2 ** n * sqrt(5))

