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
        For a 1-byte character, the first bit is a 0,
        followed by its Unicode code.
        For an n-bytes character,
        the first n bits are all one's, the n + 1 bit is 0,
        followed by n - 1 bytes with the most
        significant 2 bits being 10.

        This is how the UTF-8 encoding would work:

        _____________________________________________________________________
        |  Number of Bytes   |        UTF-8 Octet Sequence                  |
        |                    |              (binary)                        |
        |--------------------+-----------------------------------------     |
        |         1          |   0xxxxxxx                                   |
        |         2          |   110xxxxx 10xxxxxx                          |
        |         3          |   1110xxxx 10xxxxxx 10xxxxxx                 |
        |         4          |   11110xxx 10xxxxxx 10xxxxxx 10xxxxxx        |
        |___________________________________________________________________|

        x denotes a bit in the binary form of a byte that may be either 0 or 1.

        -- Leader byte for a single-byte sequence is always in the range(0-127)
        -- Leader byte for a two-byte sequence is in the range(194-223)
        -- Leader byte for a three-byte sequence is in the range(224-239)
        -- Leader byte for a four-byte sequence is in the range(240-247)

        -- Trailing byte for a two-byte sequence are in the range(128-191)
        -- Trailing byte for a three-byte sequence are in the range(128-191)
        -- Trailing byte for a four-byte sequence are in the range(128-191)

            [         xxxxxxx         xxxxxxxx           xxxxxxx       ]
                    leader byte     trailing byte     trailing byte

        You can calculate the code point value of a character by looking
        at the leader byte and the trailing bytes. For a single-byte sequence,
        the code point value is equal to the value of the leader byte.

        For a two-byte sequence,
        the code point value is equal to
            ((leader byte - 194) * 64) + (trailing byte - 128).

        For a three-byte sequence,
        the code point value is equal to
            ((leader byte - 224) * 4096) +
            ((trailing byte1 - 128) * 64) +
            (trailing byte2 - 128).

        For a four-byte sequence,
        the code point value is equal to
            ((leader byte - 240) * 262144) +
            ((trailing byte1 - 128) * 4096) +
            ((trailing byte2 - 128) * 64) +
            (trailing byte3 - 128).
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
            if cur != 1:
                return False
            i += 1
    return True
