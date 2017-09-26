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


