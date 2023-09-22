import random


min = int(input("Írd be a minimum számot: "))
max = int(input("Írd be a maximum számot: "))

szam = random.randint(min, max)
esely = random.randint(7,10)
mar_esely = 0

print("\n    ", esely, "esélyed van eltalálni a számot.\n")


while not mar_esely == esely:
    tipp = int(input("Tippeld meg a számot: "))
    mar_esely += 1
    if tipp == szam:
        print("Gratulálok a(z) ", mar_esely, ". próbálkozásra találtad ki a aszámot.", sep="")
        mar_esely = esely
    elif tipp > szam:
        print("A tipp nagyobb mint a szám")
    elif tipp < szam:
        print("A tipp kisebb mint a szám")
    else:
        print("A szám nem ", min, "és", max, "közé esik.")


