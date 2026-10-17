
t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    dis1=abs(arr[-1]-k)*2
    dis2=arr[0]
    dis = max(dis1, dis2)
    for i in range(n-1):
        dis = max(dis, arr[i+1] - arr[i])
    print(dis)
