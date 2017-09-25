'''
class Turtle:
    color = "green"
    weight = 10
    legs = 4
    shell = True
    mouth = "大嘴"

    def climb(self):
        print("climb haha ")
    def run(self):
        print("run gogo")
    def bite(self):
        print("bite bubu")
    def eat(self):
        print("eat yumyum")
    def sleep(self):
        print("sleep huhu")


tt = Turtle()
print(tt.climb())


class mylist(list): # 继承
    pass

list2 = mylist()
list2.append(5)
list2.append(7)
list2.append(10)
print(list2)
'''
#多态:不同对象对同一方法相应不同方法
class A:
    def fun(self):
        print("i am A")
class B:
    def fun(self):
        print("i am b")


a = A()
b = B()
print(a.fun())
print(b.fun())