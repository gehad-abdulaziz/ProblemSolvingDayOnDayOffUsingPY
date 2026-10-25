t = int(input())

for _ in range(t):
    arr_size = int(input())
    arr = list(map(int, input().split()))

    arr2 = sorted(arr)

    if arr2[0] != arr2[1]:
        print(arr.index(arr2[0]) + 1)
    else:
        print(arr.index(arr2[-1]) + 1)
