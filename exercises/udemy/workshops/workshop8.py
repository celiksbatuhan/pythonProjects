import time


def toplama(sayi1, sayi2):
    return sayi1 + sayi2

def cikarma(sayi1, sayi2):
    return sayi1 - sayi2

def carpma(sayi1, sayi2):
    return sayi1 * sayi2

def bolme(sayi1, sayi2):
    return sayi1 / sayi2

while True:
    print("""
      1) Toplama
      2) Çıkarma
      3) Çarpma
      4) Bölme
    """)

    cevap = str(input('Bir işlem seçiniz (kapatmak için "çık" yazınız): '))
    if cevap == "1":
        sayi1 = float(input("Birinci sayıyı giriniz: "))
        sayi2 = float(input("ikinci sayıyı giriniz: "))
        if sayi1 < 0 and sayi2 < 0:
            print("("+str(sayi1)+")", "+", "("+str(sayi2)+")", "=", toplama(sayi1, sayi2))
        elif sayi1 < 0:
            print("("+str(sayi1)+")", "+", sayi2, "=", toplama(sayi1, sayi2))
        elif sayi2 < 0:
            print(sayi1, "+", "("+str(sayi2)+")", "=", toplama(sayi1, sayi2))
        else:
            print(sayi1, "+", sayi2, "=", toplama(sayi1, sayi2))
    elif cevap == "2":
        sayi1 = float(input("Birinci sayıyı giriniz: "))
        sayi2 = float(input("ikinci sayıyı giriniz: "))
        if sayi1 < 0 and sayi2 < 0:
            print("(" + str(sayi1) + ")", "-", "(" + str(sayi2) + ")", "=", cikarma(sayi1, sayi2))
        elif sayi1 < 0:
            print("(" + str(sayi1) + ")", "-", sayi2, "=", cikarma(sayi1, sayi2))
        elif sayi2 < 0:
            print(sayi1, "-", "(" + str(sayi2) + ")", "=", cikarma(sayi1, sayi2))
        else:
            print(sayi1, "-", sayi2, "=", cikarma(sayi1, sayi2))
    elif cevap == "3":
        sayi1 = float(input("Birinci sayıyı giriniz: "))
        sayi2 = float(input("ikinci sayıyı giriniz: "))
        if sayi1 < 0 and sayi2 < 0:
            print("(" + str(sayi1) + ")", "*", "(" + str(sayi2) + ")", "=", carpma(sayi1, sayi2))
        elif sayi1 < 0:
            print("(" + str(sayi1) + ")", "*", sayi2, "=", carpma(sayi1, sayi2))
        elif sayi2 < 0:
            print(sayi1, "*", "(" + str(sayi2) + ")", "=", carpma(sayi1, sayi2))
        else:
            print(sayi1, "*", sayi2, "=", carpma(sayi1, sayi2))
    elif cevap == "4":
        sayi1 = int(input("Birinci sayıyı giriniz: "))
        sayi2 = int(input("ikinci sayıyı giriniz: "))
        if sayi1 < 0 and sayi2 < 0:
            print("(" + str(sayi1) + ")", "/", "(" + str(sayi2) + ")", "=", bolme(sayi1, sayi2))
        elif sayi1 < 0:
            print("(" + str(sayi1) + ")", "/", sayi2, "=", bolme(sayi1, sayi2))
        elif sayi2 < 0:
            print(sayi1, "/", "(" + str(sayi2) + ")", "=", bolme(sayi1, sayi2))
        else:
            print(sayi1, "/", sayi2, "=", bolme(sayi1, sayi2))
    elif cevap == "çık":
        break
    else:
        time.sleep(0.7)
        print("""
        Yanlış bir şeyler oldu galiba..""")
        time.sleep(1)
        print("""
        
                 artık
        
        """)
        time.sleep(1)
        print("""
        
              çok
        
        """)
        time.sleep(1.5)
        print("""
        
                               geç..
        
        """)
        time.sleep(0.5)
        break