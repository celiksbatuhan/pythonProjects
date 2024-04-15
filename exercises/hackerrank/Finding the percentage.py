sum_of_marks = 0
count = 0

n = int(input())

student_marks = {}
for i in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores

query_name = input()

for count, mark in enumerate(student_marks[query_name], start=1):
    sum_of_marks += mark

print(f"{sum_of_marks/count:.2f}")

