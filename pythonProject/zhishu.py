def primenum(a):
    if a != 2 and a % 2 == 0:
        return False
    for i in range(3 , int(a/2) , 2):
        if a % i == 0:
            return False
    return True
print(primenum(11))



