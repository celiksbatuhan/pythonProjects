sayi_1 = int(input("Birinci sayıyı giriniz: "))
sayi_2 = int(input("İkinci sayıyı giriniz: "))
sayi_3 = int(input("Üçüncü sayıyı giriniz: "))

sayilar = [sayi_1, sayi_2, sayi_3]

siralama = sorted(sayilar)

print("Girdikleriniz arasından en büyük sayı:", siralama[-1])
print("Girdikleriniz arasından en küçük sayı:", siralama[0])