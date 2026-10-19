
t = int(input())

for _ in range(t):
    size_Arr = int(input())
    listodd = []
    listeven = []

    arr = list(map(int, input().split()))

    for x in arr:
        if x % 2 == 0:
            listeven.append(x)
        else:
            listodd.append(x)

    if sum(listodd) % 2 == sum(listeven) % 2:
        print("YES")
    else:
        print("NO")
