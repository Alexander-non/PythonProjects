import random
num = 2 ** 100
x = random.randint(1, num)
starterNumber = x
while True:
    print(x)
    if x == 1:
        print("End, Kezdő szám:", starterNumber)
        break
    else:
        if x % 2 == 0:
            x = x / 2
        elif x % 2 != 0:
            x = ((x*3) + 1)