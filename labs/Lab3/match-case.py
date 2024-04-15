a='a'
while a!='x':
    print("----------\n-- MENU --\n----------")
    a=input("[c] reading two integers\n[+] addition\n[-] subtraction\n[*] multiplication\n[/] division\n[x] exit\n\nEnter your choice: ")
    match a:
        case 'c':
                n1=int(input("Enter the first number: "))
                n2=int(input("Enter the second number: "))
        case '+':
            print(f"---------------\n{n1} + {n2} = {n1+n2}\n---------------")
        case '-':
            print(f"---------------\n{n1} - {n2} = {n1-n2}\n---------------")
        case '*':
            print(f"---------------\n{n1} * {n2} = {n1*n2}\n---------------")
        case '/':
            print(f"---------------\n{n1} / {n2} = {n1/n2}\n---------------")
        case _:
            print("------------------\nPlease try again!!\n------------------")





