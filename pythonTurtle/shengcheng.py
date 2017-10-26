# yeild
'''
def Mygin():
    print("生成器被执行")
    yield 1
    yield 2


myg = Mygin()
next(myg)
next(myg)
next(myg)



a = [i for i in range(100) if not (i % 2) and (i % 3)]
print(a)

a = [i for i in range(100)  if not i % 2 and i % 3]
print(a)
'''

import sys
print(sys.path)