class A:
    pass
#a = A() #1
#b = A()
#a.arg = 1
#b.arg = 2
#print(a.arg)

#    def g(self): #2
#        return 'hello world'
#a = A()
#print(a.g())

#class B: #3
#    arg = 'Python'
#    def g(self):
#        return self.arg

#b = B()
#print(b.g())

#print(B.g(b))
#b.arg = 'spam'
#print(b.g())

#class D:  #4
#    @staticmethod
#    def test(x):
#        return x == 0

#print(D.test(1))
#f =D()
#print(f.test(0))

#class A(object):  #5
#    def __init__(self, int_val):
#        self.val = int_val + 1
#    @classmethod
#    def fromString(cls, val):
#        return cls(int(val))
#class B(A): pass
#x = A.fromString("1")
#print(x.__class__.__name__)
#x = B.fromString("1")
#print(x.__class__.__name__)

#class Point:  #6
#    def __init__(self, x, y, z):
#        self.coord = (x, y, z)
#    def __repr__(self):
#        return "Point(%s, %s, %s)" % self.coord
#p = Point(0.0, 10, 0.0)
#print(p)

class Singleton(object):
    obj = None
def __new__(cls, *dt, **mp):
    if cls.obj is None:
        cls.obj = object.__new____(cls,*dt,**mp)
    return cls.obj

obj = Singleton()
obj.attr = 12
new_obj = Singleton()
print(new_obj is obj)