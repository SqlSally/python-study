'''
class Turtle:
    color = "green"
    weight = 10
    legs = 4
    shell = True
    mouth = "大嘴"

    def climb(self):
        print("climb haha")
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


#多态:不同对象对同一方法相应不同方法

class A:
    def fun ( self ) :
        print ( "i am A" )

class B:
    def fun ( self ) :
        print ( "i am B" )


a = A ( )
b = B ( )
print(a.fun())
print(b.fun())


class Ball:
    def __init__(self, name):
        self.name = name
    def kick(self):
        print("%s i love you" %self.name )

a = Ball("Sally")
a.kick()


  
class Ball:
    def set_name(self, name):
        self.name = name
    def kick(self):
        print("%s i love you" %self.name )

a = Ball()
a.set_name("A")
print(a.kick())


# python 私有 和 公有

class Person:
    name = "xiaojiayu"

p = Person()
print(p.name)



class Person:

   def __init__(self):
       self.__name = "haha"  #私有属性
       self.age = 22

   def __get_name(self):  #私有方法
       return self.__name

   def get_age(self):
       return self.age

person = Person()
print(person.get_age())
print(person.__get_name())

'''
class Person:
    def __init__(self):
        self.__name = "xiaojiayu"
    def get_Name(self):
        return self.__name
p = Person()
print(p.get_Name())