#!/usr/bin/python3
"""
    0-minoperations.py: cminOperations(n)
"""


def copy_all(h, c, o):
    """
        copies the content of h to c
        Args:
            h: 'H'
            c: current counter
            0: operation counter
        Returns: tuple of current counter and operation counter
    """
    c = len(h)
    o += 1
    return (c, o)


def paste_(h, c, o):
    """
        pastes the content of c to h
        Args:
            h: 'H'
            c: current counter
            0: operation counter
        Returns: tuple of h and operation counter
    """
    h = 'H' * (len(h) + c)
    o += 1
    return (h, o)


def minOperations(n):
    """
        counts the operation done to perfom the given task
        Args:
            n: number of times for 'H'
        Returns: the number of operations done
    """
    if type(n) != int:
        return 0
    h = 'H'
    current = None
    operation = 0
    while True:
        if n == len(h):
            return operation
        elif n < len(h):
            return 0
        if n % len(h) != 0:
            (h, operation) = paste_(h, current, operation)
        else:
            (current, operation) = copy_all(h, current, operation)
            (h, operation) = paste_(h, current, operation)
