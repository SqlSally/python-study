
class C:
    count = 0

a = C()
b = C()
c = C()

C.count += 10


print(a.count)
print(C.count)


