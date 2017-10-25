count = 0

while True:
    count = count + 1
    number = count * 7
    if number % 2 != 1:
        continue
    if number % 3 == 2 and number % 5 == 4 and number % 6 == 5:
        print(number)
        break
