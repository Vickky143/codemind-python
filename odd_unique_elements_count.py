n=int(input())
m=list(map(int,input().split()))
k=list(set(m))
v=0
for i in k:
    if i%2!=0:
        v+=1
        
print(v)