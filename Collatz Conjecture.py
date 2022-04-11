import random
start = str(input("Would you like to use a random number or go with a custom number? (r | c): "))
if start == "r":
    randomNumber = random.randint(1, 2 ** 100)
elif start == "c":
    randomNumber = int(input("Valid number: "))
starterNumber = randomNumber
while True:
    print(randomNumber)
    if randomNumber == 1:
        print("End, Kezdő szám:", starterNumber)
        break
    else:
        if randomNumber % 2 == 0:
            randomNumber = randomNumber / 2
        elif randomNumber % 2 != 0:
            randomNumber = ((randomNumber*3) + 1)
