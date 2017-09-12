def count(*param):
    length = len(param)
    for i in range(length):
        letters = 0
        space = 0
        digit = 0
        others = 0
        for each in param[i]:
            if each.isdigit():
                digit += 1
            elif each.isalpha():
                letters += 1
            elif each.isspace():
                space += 1
            else:
                others += 1
        print( "letters:{0} space:{1} digit: {2} others:{3}" .format(letters, space, digit, others))

print(count("I love you 123"))


