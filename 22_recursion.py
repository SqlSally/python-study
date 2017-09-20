#用递归求阶乘

#写一个求阶乘的函数

#正整数阶乘指从1乘以2乘以3乘以4一直乘到所要求的数
#例如所有嘅的数是5，则阶乘式是1*2*3*4*5得到的积是120，所以120就是4的阶乘


#factorial
'''
def factorial(n):
    result = n
    for i in range(1, n):
        result *= i


    return result


number = int(input("enter a number:"))
print("factorial is :", factorial(number), end="")

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

number = int(input("enter a number:"))
result = factorial(number)
print("factorial %d" % (result))

def month(n):
    n1 = 1
    n2 = 1

    n3 = 1

    if n < 1:
        print("输入有误")
        return -1

    while (n - 2) > 0:
        n3 = n2 + n1
        n1 = n2
        n2 = n3
    return  n3

#1, 1, 2, 3, 5, 8, 13
def feb(n):

    if n < 3:
        return 1

    return feb(n - 2) + feb(n - 1)

print(feb(7))

'''
