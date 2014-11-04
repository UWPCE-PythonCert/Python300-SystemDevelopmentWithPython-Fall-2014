#!/usr/bin/env python

import sys

# A child class
# it keeps a reference to its parent.
class Child(object):
    def __init__(self, parent):
        self.parent = parent

        ## store some data so it will use appreciable memory
        ## multiply by 1234 to reduce interning
        self.data = [1234*i for i in range(100000)]


# A parent class -- holds and creates children
class Parent(object):
    def __init__(self):
        self.children = []

    def addChild(self):
        """
        Create and add a child object
        """
        child = Child(self)
        self.children.append(child)
        return child

parent = Parent()
print sys.getrefcount(parent)
child1 = parent.addChild()
print sys.getrefcount(parent)
child2 = parent.addChild()
print sys.getrefcount(parent)
del child1
del child2
print sys.getrefcount(parent)

