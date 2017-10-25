'''
string = "FishC"
it = iter(string)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))



class Fibs:
    def __init__(self):
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        return self.a

fibs = Fibs()
for each in fibs:
    if each < 20:
        print(each)
    else:
        break
'''

class Fibs:
    def __init__(self, n =10):
        self.a = 0
        self.b = 1
        self.n = n

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > self.n:
            raise StopIteration
        return self.a

fibs = Fibs()
for each in fibs:
    if each < 20:
        print(each)
    else:
        break
