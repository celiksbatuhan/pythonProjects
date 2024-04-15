import random

isiklar = ["kırmızı", "yeşil", "sarı"]

su_anki_isik = isiklar[random.randint(0, 2)]

if su_anki_isik == "kırmızı":
    print("Dur!")
elif su_anki_isik == "sarı":
    print("Hazır ol!")
elif su_anki_isik == "yeşil":
    print("Geç!")