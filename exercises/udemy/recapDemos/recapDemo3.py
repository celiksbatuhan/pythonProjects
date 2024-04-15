sayi = int(input("Bir sayı giriniz: "))

for i in range (2, sayi+1):
    asal = sayi % i
    if sayi == 2:
        print("Sayı asal")
        break
    elif asal == 0:
        print("Sayı asal değil")
        break
    else:
        print("Sayı asal")
        break