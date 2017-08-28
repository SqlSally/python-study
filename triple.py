a, b, x, y, z = 6, 5, 4, 1, 0

def min(x, y):
    return x if x < y else y

small = min(min(min(min(x, y), z), a), b)
print(small)
