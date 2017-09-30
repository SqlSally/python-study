

class New_int(int):
    def __add__(self, other):
        return int.__sub__(self, other)

    def __sub__(self, other):
        return int.__add__(self, other)


a = New_int(1)
b = New_int(2)

print(a.__add__(2))
print(b.__sub__(3))
