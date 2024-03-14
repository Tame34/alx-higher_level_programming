#!/bin/bash/python3

def uppercase(s):
    for char in s:
        uppercase_char = char
        if ord('a') <= ord(char) <= ord('z'):
            uppercase_char = chr(ord(char) - 32)
        print(uppercase_char, end='')
    print()

# Example usage:
uppercase("hello")

