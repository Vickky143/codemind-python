n=int(input())
m=list(map(int,input().split()))
k=int(input())
c=0
for i in m:
    if i==k:
        c+=1
print(c)