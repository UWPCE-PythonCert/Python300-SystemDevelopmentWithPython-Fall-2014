#!/usr/bin/env python

"""mutable kwarg failure demo"""

def add_plus_one(values=[]):
    """adds the values in values together, plus 1"""
    values.append(1)
    return sum(values)

print add_plus_one()
print add_plus_one([1, 2, 3])
print add_plus_one()
