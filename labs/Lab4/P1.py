import os
import re

array = []

while True:
    os.system('cls')
    print("""
1. Citire sir de caracatere de la tastatura.
2. Afisare sir citit.
3. Afisarea nr total de cuvinte din sir, cuvintele si a nr. de caractere pentru fiecare cuvant.
4. Inlocuire caracterului <<X>> in sirul initial cu caracterul <<Y>>.
5. Construiti un sir nou format din caracterele majuscule din sirul initial.
6. Afisati numarul de aparitii pentru fiecare vocala din sirul initial.
7. Eliminati caracterele speciale din sirul initial.
8. Afisati INTREG sirul de caractere pornid de la o pozitie X.
9. Exit
    """)
    choice = int(input("Enter a choice: "))
    match choice:
        case 1:
            print("\n1.\n------------------------------------------------")
            array = list(input("Enter a sentence: ").split())
        case 2:
            print("\n2.\n------------------------------------------------")
            print(array)
            input("Press Enter to continue...")
        case 3:
            count2 = 1
            print("\n3.\n------------------------------------------------")
            for i in array:
                count1 = 0
                for j in i:
                    count1 += 1
                print(f"{count2}.{i} - {count1}")
                count2 += 1
            input("Press Enter to continue...")
        case 4:
            count3 = 0
            x = input("x: ")
            y = input("y: ")
            for i in array:
                array[count3] = i.replace(y.upper(), x.upper())
                count3 += 1
            count3 = 0
            for i in array:
                array[count3] = i.replace(y.lower(), x.lower())
                count3 += 1
        case 5:
            print("\n5.\n------------------------------------------------")
            new_sentence = ""
            alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            for i in array:
                for j in i:
                    if j in alphabet:
                        new_sentence += j
            print(new_sentence)
            input("Press Enter to continue...")
        case 6:
            count5 = 1
            vocals = 'aeiou'
            print("\n6.\n------------------------------------------------")
            for i in array:
                print(f"{count5}.{i} - ", end='')
                count5 += 1
                for j in vocals:
                    count6 = 0
                    for k in i:
                        if k.lower() == j.lower():
                            count6 += 1
                    if count6 != 0:
                        print(f"({count6}x{j})", end='')
                print()
            input("Press Enter to continue...")
        case 7:
            count7 = 0
            for i in array:
                array[count7] = re.sub(r'[^a-zA-Z\s]', '', i)
                count7 += 1
        case 8:
            sentence = ""
            x = int(input("x: "))
            for i in range(len(array)):
                sentence += array[i]
                if i != len(array)-1:
                    sentence += ' '
                else:
                    sentence += '.'
            print(sentence[x:], end='')
            print(sentence[:x])
            input("Press Enter to continue...")
        case 9:
            break
