result = 0
n = int(input("Enter a number between [20, 50): "))
if 20 <= n < 50:
    if n % 2 != 0:
        print(int((n+1)/2))
    else:
        print(f"-{n/2}")
#     for i in range(1, n+1):
#         if i % 2 == 0:
#             print(f"{i}", end='')
#             result -= i
#             if i != n:
#                 print("+", end='')
#         else:
#             print(f"{i}", end='')
#             if i != n:
#                 print("-", end='')
#             result += i
#
# print(f" = {result}")
