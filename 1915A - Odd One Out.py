t = int(input())

for _ in range(t):
    listt = list(map(int, input().split()))
    if listt.count(listt[0])==1:
        print(listt[0])
    elif listt.count(listt[1])==1:
        print(listt[1])
    else:
        print(listt[2])
