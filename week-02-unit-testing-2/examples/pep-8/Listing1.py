#!/usr/bin/env python
# coding: utf-8
"""
"""

import string
import string


module_variable = 0
unused_variable = None

float = 1.0

long = "loooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooong"        
breakable_long_line = 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1


def functionName(self, int, unused_local=None):
    module_variable = 5*5
    return module_variable

print functionName(None,None)

class my_class(object):

    def __init__(self, arg1, string):
        self.value = True
        return

    def method1(self, str):
        return self.value

    def method2(self):
        return
        print 'How did we get here?'
        
    def method3(self):
        self.s = str

    
    def method1(self):
        return self.value + 1
    method2 = method1
    
class my_subclass(my_class):
    
    def __init__(self, arg1, string):
        self.value = arg1
        return


class Food(object):
    def __init__(self):
        unused_local = None
        self.unused_data_member = None


class Pizza(Food):
    pass

# test recommendations from http://legacy.python.org/dev/peps/pep-0008/#programming-recommendations

# http://legacy.python.org/dev/peps/pep-0008/#constants
food = Food()
pizza = Pizza()

print "type(food) == type(pizza): %s" % (type(food) == type(pizza))
print "isinstance(food, Food): %s" % isinstance(food, Food)
print "isinstance(pizza, Food): %s" % isinstance(pizza, Food)

# create a larger Cyclomatic complexity, error triggered with
# flake8 --max-complexity=5
def f(x):
    if x is 1:
        return x
    elif x is 2:
        return x
    elif x is 3:
        return x
    elif x is 4:
        return x
    elif x is 5:
        return x

print "f(5): %s" % f(5)
