'''

class C:
    def __init__(self):
        self.y = "x - man"
c = C()

print(c.y)

print(getattr(c,"x","true"))


class C:
    def __int__(self, size = 10):
        self.size = size

    def getSize(self):
        return self.size

    def setSize(self, value):
        self.size = value

    def delSize(self):
        del self.size
        print("i hate you")

    x = property(getSize, setSize, delSize)

c = C()
c.x = 2
print(c.x)
print(c. size)



class C:

    def __getattribute__(self, name):
        print("getattribute")
        return super().__getattribute__(name)

    def __getattr__(self, name):
        print("getattr")




    def __setattr__(self, name, value):
        print("setattr")
        super().__setattr__(name, value)

    def __delattr__(self, name):
        print("delattr")
        super().__delattr__()


c = C()
c.x = 1
print(c.x)



#写一个矩形类，默认有宽和高两个属性
#如果为一个叫做square的属性赋值，那么说明这是一个正方形，值就是正方形的边长，此时宽和高应该等于边长

class Rectangle:

    def __init__(self, width = 0, height = 0):
        self.width = width
        self.height = height

    def __setattr__(self, name, value):
        if name == "square":
            self. width = name
            self. height = name

        else:
            super().__setattr__(name, value)

    def getArea(self):
        return self.width * self.height

r = Rectangle(4,5)
print(r.getArea())
'''



























