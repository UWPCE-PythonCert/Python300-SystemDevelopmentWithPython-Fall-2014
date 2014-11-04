#!/usr/bin/env python

class Foo(object):
    # __metaclass__ = NameMangler
    def __new__(cls, *args, **kwargs):

        uppercase_attr = {}
        for name in dir(cls):
            if not name.startswith('__'):
                setattr(cls, name.upper(), getattr(cls, name))

        return super(Foo, cls).__new__(cls)

    x = 1

if __name__ == "__main__":
    f = Foo()
    f.x = 1
    print f.x
    print f.X
