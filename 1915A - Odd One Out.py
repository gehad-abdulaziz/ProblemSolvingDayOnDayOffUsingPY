t = int(input())

for _ in range(t):
    a, b, c = map(int, input().split())
    if a==c &a!=b:
        print(b)
    elif a==b &a!=c:
        print(c)
    else:
        print(a)
