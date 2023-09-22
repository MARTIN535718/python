a = int(input("Írj be egy számot az x^2 értékének: "))
b = int(input("Írj be egy számot az X értékének. Ha nem akarsz értéket adni nyomjegy spacet: "))
c = int(input("Írj be egy számot a C értéknek: "))

fuggveny_kiszam = (b * b) - 4 * a * c
if fuggveny_kiszam > 0:
    fuggveny_kiszam = fuggveny_kiszam ** 0.5
    x1 = (-(b) + fuggveny_kiszam) / (2 * a)
    x2 = (-(b) - fuggveny_kiszam) / (2 * a)
    print("Az x1 értéke: ", x1, ", az x2 pedig: ", x2, ".", sep="")    
else:
    print("A szám ami kijött negatív ezért nincs megoldása.")

