n = int(input())
arr = list(map(int, input().split()))
if len(arr) == n:
    arr_set = set(arr)
    arr_list = list(arr_set)
    result = sorted(arr_list)
    print(result[-2])
else:
    print("Count of the numbers you entered is less or greater than \"n\".")
