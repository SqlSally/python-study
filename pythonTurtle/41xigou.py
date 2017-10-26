

'''

class CapStr(str):
    def __new__(cls, string):
        string = string.upper()
        return str.__new__(cls, string)


a = CapStr("I love FishC.com!")
print(a)

class C:
    def __init__(self):
        print("我被init调用")

    def __del__(self):
        print("我是del，我被调用")

c1 = C()
c2 = c1
del c2
'''



