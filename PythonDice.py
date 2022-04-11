import random
while True:
    answer = ""
    print("\nYou have rolled:", random.randrange(1, 6))
    while answer != "y" and answer != "n": answer = input("Do you want to roll again? (y | n) \n").lower()
    if answer == "y": print("\nYou have rolled:", random.randrange(1, 6))
    else: print("Too bad!")
    continueGuard = str(input("Do you want to continute? (y | n): ")).lower()
    while continueGuard != "y" and continueGuard != "n": continueGuard = str(input("Do you want to continute? (y | n): ")).lower()
    if answer == "y": print("\nYou have rolled:", random.randrange(1, 6))
    else: quit()