class Countlist:
    def __init__(self,*args:):
        self.value = [x for x in args]  #列表推到式
        self.count = {}.fromkeys(range(len(self.values)), 0)


    def __len__(self):
        return len(self. values)

    def __getitem__(self, key):
        self.count[key] += 1
        return self.value[key]


