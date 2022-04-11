Num = int(input("Enter a number: "))
PrimeList = []
for x in range(Num + 1):
    if (Num % (x+1)) == 0: #Le checkolom hogy mik az osztói
        PrimeList.append(x+1)
if len(PrimeList) <= 2:
    print("Prime number")
else:
    print("Not a prime number")