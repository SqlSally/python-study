''''
class Turtle:
    def __init__(self, x):
        self.num = x            # 传入多少参数证明有多少只乌龟


class Fish:                    # 传入多少参数证明有多少只鱼
    def __init__(self, x):
        self.num = x


class Pool:
    def __init__(self, x, y):
        self.turtle = Turtle(x)
        self.fish = Fish(y)

    def print_num(self):
        print("水池里总共有乌龟%d只，小鱼%d 条！" %(self.turtle.num, self.fish.num))

pool = Pool(4, 5)
print(pool.print_num())


class C:
    count = 0

a = C()
b = C()
c = C()

C.count += 10


print(a.count)
print(C.count)
'''



