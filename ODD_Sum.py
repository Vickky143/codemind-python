n=int(input())
m=list(map(int,input().split()))
a=0
for i in range(0,len(m)):
    if m[i]%2!=0:
        a+=m[i]
print(a)