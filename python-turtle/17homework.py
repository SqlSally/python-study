


def huiwen(text):
    for each1 in range(len(text) - 1):
        if text[each1] != text[len(text) - 1 - each1]:
            return False
    return True

print(huiwen("abbcbba"))

def huiwen(text):
    a = list(text)
    b = list(reversed(a))
    if a == b:
        return True
    else:
        return False


print(huiwen("abc"))
