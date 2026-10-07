x, k = map(int, input().split())
counter=0
remaining=(4*60) - k
for i in range(1,x+1):
    if remaining-i*5>=0:
        counter+=1
        remaining-=i*5
    else:
        break
print(counter)
