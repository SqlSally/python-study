'''
def isLeapYear(n):
    if n % 4 == 0 and n % 100 != 0:
        print("it is Ryear")
    elif  n % 400 == 0:
        print( "it is Ryear")
    else:
        print( "it is not")



print(isLeapYear(400))
print(isLeapYear(2000))
print(isLeapYear(1990))
print(isLeapYear(1900))
print(isLeapYear(1952))
print(isLeapYear(2003))


n = int(input("please enter the year:"))
print("it is Ryear") if (n % 4 == 0 and n % 100 != 0) or (n % 400 == 0) else print("it is not")


def isLeapYear(n):
    return n % 400 == 0 or n % 4 == 0 and n % 100 != 0
'''

