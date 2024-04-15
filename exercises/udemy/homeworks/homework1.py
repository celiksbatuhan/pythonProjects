sayi1 = int(input("1. sayıyı giriniz: "))
sayi2 = int(input("2. sayıyı giriniz: "))

if sayi1 > sayi2:
    print(sayi1, ">", sayi2)
elif sayi2 > sayi1:
    print(sayi2, ">", sayi1)
elif sayi1 == sayi2:
    print(sayi1, "=", sayi2)
else:
    print("Bir şeyler yanlış gitti..")
