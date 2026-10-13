n=int(input())
for _ in range(n):
    k, r, c = map(int, input().split())
    if k + r == c:
        print("+")
    else:
        print("-")
