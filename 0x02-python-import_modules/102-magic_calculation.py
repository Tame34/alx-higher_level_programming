#!/usr/bin/python3
# 102-magic_calculation.py task


def magic_calculation(a, b):
    """Match bytecode apready provided."""
    from magic_calculation_102 import add, sub

    if a < b:
        c = add(a, b)
        for i in range(4, 6):
            c = add(c, i)
        return (c)

    else:
        return (sub(a, b))
