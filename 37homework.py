

#如果不希望对象的属性或方法被外部直接引用，我们可以怎么做？

#在名字前面加上双下划线,
#getName 称之为『访问器』
'''
class Person:
    __name = "小甲鱼"
    def getName(self):
        return self.__name

p = Person()
print(p.getName())


class Person:
    __name = "小甲鱼"

p = Person()
print(p._Person__name)


#类的实例化哪个方法会被自动调用

class MyClass:
    name = "fishic"
    def myFun(self):
        return self.name

n = MyClass()
print(n.myFun())


#计算两个成人和一个小孩子weekday里面的票价?
#weekend 票价将涨价平时的1.2 倍
#child的话，打折为半价


class Ticket:
    def __init__(self, weekend = False, child = False):
        self.exp = 100
        if weekend:
            self.inc = 1.2

        else:
            self.inc = 1


        if child:
            self.discount = 0.5

        else:
            self.discount = 1

    def calcPrice(self, num):
        return self.exp * self.discount * self.inc * num


adult = Ticket()
child = Ticket(child = True)
print("2个成人+1个小孩平日票价为 %s " %(adult.calcPrice(2) + child.calcPrice(1)))

'''






















