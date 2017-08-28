import sys, traceback

specials = '~!@#$%^&*()_=-/,.?<>;:[]{}|\\'

def hasNumber(password):
    return any(c.isdigit() for c in password)

def hasAlpha(password):
    return any(c.isalpha() for c in password)

def isSpecial(char):
    return char in specials

def hasSpecial(password):
    return any(isSpecial(c) for c in password)

def isLow(password):
    return password.isalnum() and len(password) <= 8

def isMedium(password):
    return len(password) > 8 and (hasAlpha(password) + hasSpecial(password) + hasNumber(password)) == 2

def isHigh(password):
    return len(password) > 15 and (hasAlpha(password) + hasSpecial(password) + hasNumber(password)) == 3 and password[0].isalpha()



inputPassword = input('Please enter test password: ')
if isLow(inputPassword):
    print('You are low, please do...')
    sys.exit(0)
if isMedium(inputPassword):
    print('You are medium, please do...')
    sys.exit(0)
if isHigh(inputPassword):
    print('You are high, which is good')
    sys.exit(0)
print('something weird is typed, please check')
