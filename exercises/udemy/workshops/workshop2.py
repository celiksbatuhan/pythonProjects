mil = 1.609344
km = 0.621371192

print("1) Mil ==> Kilometre")
print("2) Kilometre ==> Mil")

cevap = input("Hangisi?: ")

if cevap == "1":
    a = float(input("Bir değer giriniz: "))
    b = a * mil
    print(a, "Mil", b, "Kilometre eder")
elif cevap == "2":
    a = float(input("Bir değer giriniz: "))
    b = a * km
    print(a, "Kilometre", b, "Mil eder")
else:
    print("Ne yaptın sen..")