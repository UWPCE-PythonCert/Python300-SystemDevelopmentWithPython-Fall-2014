
# this function can not be pickled due to the requirement:
# - "functions defined at the top level of a module"
# see https://docs.python.org/2/library/pickle.html#what-can-be-pickled-and-unpickled

def foo():
    def bar():
        return 2

    return bar
