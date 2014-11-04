class A(object):
    def my_method(self):
        print "doing A's stuff"
    
class B(A):
    def my_method(self):
        A.my_method(self)
        print "doing B's stuff"
    
class C(A):
    def my_method(self):
        A.my_method(self)
        print "doing C's stuff"

class D(B,C):    
    def my_method(self):
        super(D,self).my_method()
        print "doing D's stuff"


if __name__ == '__main__':
    a = A()
    a.my_method()

    print
    b = B()
    b.my_method()

    print
    c = C()
    c.my_method()

    print 
    d = D()
    d.my_method()

