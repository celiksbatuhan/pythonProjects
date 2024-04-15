count = 0

s1 = input("Enter the first sentence: ")
s2 = input("Enter the second sentence: ")

for i in s1.lower():
    if i in s2.lower():
        count += 1

if count == len(s1):
    print("First and  second sentences are balanced.")