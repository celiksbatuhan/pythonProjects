cumle = str(input("Bir cümle giriniz: "))

kelimeler = cumle.split()
alfabetik = sorted(kelimeler, key=str.lower)
for kelime in alfabetik:
    print("-", kelime)