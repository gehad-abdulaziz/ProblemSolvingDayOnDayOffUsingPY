t = int(input())

for _ in range(t):
    a, b = map(int, input().split())
    c = abs(a - b)
    res= c// 10

    if c% 10 != 0:
        res += 1

    print(res)
