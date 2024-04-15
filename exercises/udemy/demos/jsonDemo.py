import json

with open("jsonDemo.json") as users:
    data = json.load(users)
    print("--------------------------")
    for i in range(5):
        print(f'• {data[i]["username"]}')
        print(f'• {data[i]["email"]}')
        print(f'• {data[i]["address"]["city"]}')
        print(f'• {data[i]["address"]["geo"]["lat"]}')
        print(f'• {data[i]["address"]["geo"]["lng"]}')
        print("--------------------------")