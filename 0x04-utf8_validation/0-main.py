#!/usr/bin/python3
"""
Main file for testing
"""

#  bin(123)  --  to print a number in binary
#  to print in a colorful way -- __import__('click').echo(__import__('click').style(f'{data}', fg='blue'))

validUTF8 = __import__('0-validate_utf8').validUTF8

data = [65]
print(validUTF8(data))

data = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
print(validUTF8(data))

data = [229, 65, 127, 256]
print(validUTF8(data))