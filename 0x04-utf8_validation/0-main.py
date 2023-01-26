#!/usr/bin/python3
"""
Main file for testing
"""

#  bin(123)  --  to print a number in binary

validUTF8 = __import__('0-validate_utf8').validUTF8

data = [65]
__import__('click').echo(__import__('click').style(f'{data}', fg='blue'))
if validUTF8(data):
    __import__('click').echo(__import__('click').style('True', fg='green'))
else:
    __import__('click').echo(__import__('click').style('False', fg='red'))

data = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
__import__('click').echo(__import__('click').style(f'{data}', fg='blue'))
if validUTF8(data):
    __import__('click').echo(__import__('click').style('True', fg='green'))
else:
    __import__('click').echo(__import__('click').style('False', fg='red'))

data = [229, 65, 127, 256]
__import__('click').echo(__import__('click').style(f'{data}', fg='blue'))
if validUTF8(data):
    __import__('click').echo(__import__('click').style('True', fg='green'))
else:
    __import__('click').echo(__import__('click').style('False', fg='red'))
