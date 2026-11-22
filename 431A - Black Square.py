a1 , a2  , a3  , a4= map(int, input().split())
s=input()
len_s = len(s)
sum=0
for i in range(len_s):
    if s[i] == '1':
        sum=sum + a1
    elif s[i] == '2':
        sum=sum + a2
    elif s[i] == '3':
        sum=sum + a3
    elif s[i] == '4':
        sum=sum + a4
print(sum)
