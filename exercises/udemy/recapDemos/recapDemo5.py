import sys

list = ['Mahsun', 'Bir', 'Pezevenk', 31, 'sjsj', 0]

for i in list:
    try:
        print("Sayı:", i)
        result = 1 / int(i)
        print("Sonuç:", result)
    except ValueError:
        print("Kelimeler ile matematiksel işlem yapılamaz.")
    except ZeroDivisionError:
        print("Payda 0 olamaz aga, matematik bu kusura bakma :(")
    except:
        print(i, "Sonuç hesaplanamadı..")
        print("Sstem diyor ki:", sys.exc_info()[0])