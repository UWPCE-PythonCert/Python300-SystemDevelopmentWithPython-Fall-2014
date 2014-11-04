class Watcher(type):
    def __init__(cls, name, bases, clsdict):
        if len(cls.mro()) > 2:
            print("was subclassed by " + name)
        super(Watcher, cls).__init__(name, bases, clsdict)

class SuperClass:
    __metaclass__ = Watcher

class SubClass(SuperClass):
  pass

sub_class = SubClass()
