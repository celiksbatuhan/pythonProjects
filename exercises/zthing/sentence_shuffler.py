import random

sentence = list(map(str, input("Enter a sentence: ").split()))
random.shuffle(sentence)
for word in sentence:
    print(word, end=" ")