ogrenciler = ["Ayşe", "Fatma", "Hayriye", "Ali", "Veli", "Kırk Dokuz", "Elli"]
a = open("ogrenciler.txt", "a")

for ogrenci in ogrenciler:
    a.write(ogrenci)
    a.write("\n")

a.close()
