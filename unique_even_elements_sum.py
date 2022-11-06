n=int(input())
m=list(map(int,input().split()))
k=set(m)
v=0
for i in k:
    if i%2==0:
        v+=i
print(v)