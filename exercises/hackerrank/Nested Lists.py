n = int(input())
records = [['' for i in range(2)] for j in range(n)]
if 2 <= n <= 5:
    names = ['' for i in range(n)]
    scores = ['' for i in range(n)]
    for i in range(n):
        name = input()
        records[i][0] = name
        score = float(input())
        records[i][1] = score

    for i in range(n):
        scores[i] = records[i][1]

    sorted_scores = list(sorted(set(scores)))
    j = 0

    for i in range(n):
        if records[i][1] == sorted_scores[1]:
            names[j] = records[i][0]
            j += 1

    result = sorted(names)

    for i in result:
        if i != '':
            print(i)
