n=int(input())
m=list(map(int,input().split()))
for i in range(len(m)):
    if m[i]%2!=0:
        v=m[i]
print(v)