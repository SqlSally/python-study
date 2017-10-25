class MyDescriptor:
    def __get__(self, instance, owner):
        print("getting...",self,instance,owner)

     def __set__(self, instance, owner):
        print("setting...", self, instance, owner)

    def __delete__(self, instance):
        print("deleting..", self, instance, owner)


class Test:
    x = MyDescriptor()
    