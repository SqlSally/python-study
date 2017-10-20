#第 0001 题：做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用生成激活码（或者优惠券），
# 使用 Python 如何生成 200 个激活码（或者优惠券）？
'''
from random import Random

def codeGenerator(number, codeLength = 10):
#    print('**** Code Generator ****')
    codeFile = open('codes.txt', 'w')
    if number <= 0:
        return 'invalid number of codes'
    else:
        chars = 'abcdefghijklmnopgrstuvwxyzABCDEFGHIJKLMNOPGRSTUVWXYZ1234567890'

        random = Random()
        for j in range(1, number+1):
            str = ''
            for i in range(1, codeLength+1):
                index = random.randint(1, len(chars))
                str = str + chars[index-1]
            codeFile.write(str+'\n')

print(codeGenerator(200))
'''

from random import Random

def codeRandom(number, codeLength = 10):
    codeFile = open("code200","w")
    if number <= 0:
        return "invalid number of codes"
    else:
        chars = "abcdefghijklmnopgrstuvwxyzABCDEFGHIJKLMNOPGRSTUVWXYZ1234567890"
        coderandom = Random()
        for i in range(0, number + 1):
            str = ""
            for j in range(0, codeLength + 1 ):
               index = coderandom.randint(0 , len(chars))
               str  = str + chars[index - 1]
            codeFile.write(str + "\n")

print(codeRandom(200))