class MyClass(object):
    def __init__(self, *args, **kwargs):
        pass

    def __new__(cls, *args, **kwargs):
        print "creating new class %s" % cls
        return super(MyClass,cls).__new__(cls, *args, **kwargs)

o = MyClass(1, key=2)
