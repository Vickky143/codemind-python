a=int(input())
lst=list(map(int,input().split()))
c=[]
d=[]
for i in range(len(lst)):
    if i%2==0:
        c.append(lst[i])
    else:
        d.append(lst[i])
if sum(c)==sum(d):
    print("YES")
else:
    print("NO")