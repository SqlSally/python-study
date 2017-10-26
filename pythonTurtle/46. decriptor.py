class MyDescriptor:
    def __get__(self, instance, owner): #用于访问属性，他返回属性的值
        print("get...",self, instance, owner)
    def __set__(self, instance, value):
        print("set...", self, instance, value)
    def __delete__(self, instance):
        print("delete", self, instance)

class Test:
    x = MyDescriptor # MyDescriptor 是x 的描述符

test = Test()
print(test.x)