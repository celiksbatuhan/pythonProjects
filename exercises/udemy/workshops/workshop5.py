sayi = int(input("Bir sayı giriniz: "))

faktoriyel = 1

for i in range(1, sayi+1):
    faktoriyel = faktoriyel * i

print(sayi, "faktöriyel =", faktoriyel)