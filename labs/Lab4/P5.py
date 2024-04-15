text = list((input("Enter a text: ").split()))
n = int(input("Enter n: "))
for i in text:
    if len(i) == n:
        print(i)