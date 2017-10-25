import random

times = 3
secret = random.randint(1, 10)

print("猜猜数字:", end=" ")

while times > 0:
    guess = int(input())
    times = times - 1

    if guess == secret:
        print("你是小甲鱼心中的蛔虫么")
        print("猜中了也没有奖励")
        break

    #Tell player where to guess
    if guess > secret:
        print("哥，大了大了")
    else:
        print("嘿嘿，小了，小了！！")

    #See if there is more times
    if times <= 0:
        print("机会用完了哦")
        break
    print("再试一次：", end=" ")


print("游戏结束了")
