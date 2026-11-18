a = int(input())
for q in range(a):
    n, m = map(int, input().split())
    x = input()
    s = input()
    res = -1
    for i in range(6):
        if s in x:
            res = i
            break
        x += x
    print(res)
