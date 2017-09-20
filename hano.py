
#汉诺塔通过把x柱子上的盘子移动到z柱子上，从小到大
def hanoi(n, x, y, z): #n 有多少个盘子, x柱子， y柱子，z柱子
    if n == 1:
        print(x, "--->" ,z)
    else:
        hanoi(n-1, x, z, y)#将前n-1个盘子从x移动到y上
        print(x, "---->", z) #将最低下的最后一个盘子从x移动到z上
        hanoi(n-1, y, x, z)#将y上的n-1个盘子移动到z上

n = int(input("请输入汉诺塔的层数："))
print(hanoi(n, "x","y","z"))  