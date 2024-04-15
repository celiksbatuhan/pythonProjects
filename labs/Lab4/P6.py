import re

text = input("Enter a text: ")
new_text = re.sub(r'[^a-zA-Z\s]', '', text)
print(new_text)