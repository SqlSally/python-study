'''
class A:
    pass
class B(A):
    pass
print(issubclass(B,A))
print(issubclass(B,B))
print(issubclass(B,object))

b1 = B()

print(isinstance(b1,A))


class C:
    def __init__(self, x=0):
        self.x = x


c1 = C()
print(hasattr(c1, "x"))


print(getattr(c1,"x"))  #因为x默认为0，所以返回0


print(getattr(c1,"y","您所访问的参数不存在"))  #因为x默认为0，所以返回0


print(setattr(c1,"y",2))
print(getattr(c1,"y"))

'''

class C:
    def __init__(self, size =10):
        self.size = size

    def getSize(self):
        return self.size

    def setSize(self, value):
        self.size = value

    def delSize(self,size):
        del self.size

    x = property(getSize, setSize, delSize)

c1 = C()
print(c1.x)
c1.x = 18
print(c1.x)

del c1.x


