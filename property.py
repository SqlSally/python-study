'''

class C:
    def __init__(self):
        self.y = "x - man"
c = C()

print(c.y)

print(getattr(c,"x","true"))

'''
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

    x = property(getSize, setSize)

c = C()
c.x = 2
print(c.x)
print(c. size)

'''
