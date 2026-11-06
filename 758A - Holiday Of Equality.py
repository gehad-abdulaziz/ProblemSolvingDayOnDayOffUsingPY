
t = int(input())
listt = list(map(int, input().split()))
min=max(listt)
min_count = listt.count(min)
count=0
for i in range (t):
    if(listt[i]<min):
        count=count+(min-listt[i])

print(count)
