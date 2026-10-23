
t = int(input())

for _ in range(t):
    size_Arr = int(input())
    arr = sorted(map(int, input().split()))

    if size_Arr == 1:
        print("YES")
        continue

    possible = True

    for i in range(size_Arr - 1):
        if arr[i + 1] - arr[i] > 1:
            possible = False
            break

    if possible:
        print("YES")
    else:
        print("NO")
