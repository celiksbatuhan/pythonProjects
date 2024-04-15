text = list(input("Enter a text: ").split())
word = input("Enter the word: ")

for i in text:
    if i.lower() == word.lower():
        print(i)
