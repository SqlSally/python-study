#第 0004 题： 任一个英文的纯文本文件，统计其中的单词出现的个数。
'''
import re
def getnum():
    num = 0
    myfile = open("word.txt", "r")
    for line in myfile.readlines():
        num += len(re.findall(r'[o]+', line))
    myfile.close()
    return num
print(getnum())
'''
