#!/bin/bash/python3
# 6-print_comb3.py

# Print all possible different combinations of two digits in ascending order.
# The two digits must be different - 01 and 10 are considered identical.

# Using a list comprehension to generate the combinations
combinations = ["{}{}".format(digit1, digit2) for digit1 in range(0, 10) for digit2 in range(digit1 + 1, 10)]

# Joining the combinations with a comma and space
print(", ".join(combinations))
