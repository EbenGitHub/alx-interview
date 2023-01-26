#!/usr/bin/python3
"""
Main file for testing
"""

#  bin(xxx)  --  to print a number in binary
#  hex(xxx)  --  to print a number in hexadecimal
#  eval(xxx)  --  to print a number in decimal

#  to print in a colorful way -- __import__('click').echo(__import__('click').style(f'{data}', fg='blue'))

# Bin: 0b10000000 0b01000000 0b00100000 0b00010000 0b00001000 0b00000100 0b00000010 0b00000001
# Int: 128        64         32         16         8          4          2          1
# Hex: 0x80       0x40       0x20       0x10       0x8        0x4        0x2        0x1

validUTF8 = __import__('0-validate_utf8').validUTF8

data = [65]
print(validUTF8(data))

data = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
print(validUTF8(data))

data = [229, 65, 127, 256]
print(validUTF8(data))