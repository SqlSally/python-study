'''
def triangle(n):
    for i in range (n):
        for j in range(i+1):
            print("*", end=" ")
        print()
    print()

print(triangle(5))

def triangle(n):
    for i in range (n,0,-1):
        for j in range(i):
            print("*",end=" ")
        print()
    print()
print(triangle(5))


def triangle(n):
    for i in range(n, 0, -1):
        print(" " * (i-1) , end="")
        for j in range(n - (i-1)):
            print("*", end="")
        print()

print(triangle(10))

'''
def triangle(n):
    for i in range (n):
        print(" " * i , end="")
        for j in range(n-i):
            print("*",end="")
        print()
        
print(triangle(10))