'''
#调用父类

class Parent:
    def hello(self):
        print("正在调用父类方法")

class Child(Parent):
    pass

p = Parent()
print(p.hello())

c = Child()
print(c.hello())

class Child(Parent):  #
    def hello(self):
        print("正在调用子类的方法")

d = Child()
print(d.hello())



import random as r

class Fish:
    def __init__(self):
        self.x = r.randint(0, 10)
        self.y = r.randint(0, 10)

    def move(self):
        self.x -= 1
        print("我的位置是：", self.x, self.y)


class Carp(Fish):
    pass

class Salmon(Fish):
    pass

class Shark(Fish):
    def __init__(self):
        super().__init__()
        self.hungry = True

    def eat(self):
        if self.hungry:
            print("吃货的梦想是天天有的吃")

        else:
            print("吃不下了")


fish = Fish()
print(fish.move())
shark = Shark()
print(shark.move())

'''

class Base1:
    def foo1(self):
        print("我是foo1，我为base1代言")

class Base2:
    def foo2(self):
        print("我是foo2，我为base2代言")

class C(Base1, Base2):
    pass

c = C()
print(c.foo1())
print(c.foo2())