RED = 3
BLUE = 3
YELLOW = 6
TOTAL = 8

# Red is 0, Blue 2 -> 3
# Red is 1, Blue 1 -> 3
# Red is 2, Blue 0 -> 3
# Red is 3, Blue 0 -> 3

# TOTAL - red - blue



for r in range(0, RED + 1):
    for b in range(max(TOTAL - r - YELLOW, 0), BLUE + 1):
        y = TOTAL - r - b
        print("There are {0} red, {1} blue and {2} yellow balls".format(r, b, y))
