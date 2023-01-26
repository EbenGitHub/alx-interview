#!/usr/bin/python3
"""
    UTF-8-validation:
    Given an integer array data representing the data, 
    return whether it is a valid UTF-8 encoding 
    (i.e. it translates to a sequence of valid UTF-8 encoded characters).
"""


def validUTF8(data):
    """
        A character in UTF8 can be from 1 to 4 bytes long.
        For a 1-byte character, the first bit is a 0, followed by its Unicode code.
        For an n-bytes character, the first n bits are all one's, the n + 1 bit is 0, 
        followed by n - 1 bytes with the most significant 2 bits being 10.

        This is how the UTF-8 encoding would work:

        _______________________________________________________________________________________
        |                    Number of Bytes   |        UTF-8 Octet Sequence                  |
        |                                      |              (binary)                        |
        |               --------------------+-----------------------------------------        |
        |                           1          |   0xxxxxxx                                   |
        |                           2          |   110xxxxx 10xxxxxx                          |
        |                           3          |   1110xxxx 10xxxxxx 10xxxxxx                 |
        |                           4          |   11110xxx 10xxxxxx 10xxxxxx 10xxxxxx        |
        |_____________________________________________________________________________________|

                        x denotes a bit in the binary form of a byte that may be either 0 or 1.
    """

    def check(num):
        mask = 1 << (8 - 1)  # 10000000
        i = 0
        while num & mask:  # 11000110 & 100000
            mask >>= 1
            i += 1
        return i

    i = 0
    while i < len(data):
        j = check(data[i])
        k = i + j - (j != 0)
        i += 1
        if j == 1 or j > 4 or k >= len(data):
            return False
        while i < len(data) and i <= k:
            cur = check(data[i])
            if cur != 1: return False
            i += 1
    return True
