vocals = "aeiouAEIOU"
new_text = ""
text = input("Enter a text: ")
if len(text) <= 100:
    for i in text:
        new_text += i
        for j in vocals:
            if i == j:
                new_text += j
print(new_text)
