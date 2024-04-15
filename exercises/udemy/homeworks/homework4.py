ogrenciler = str(input("Lütfen öğrencilerin isimlerini boşluk bırakarak giriniz: "))
liste = ogrenciler.split()

for ogrenci in liste:
    print("-", ogrenci)