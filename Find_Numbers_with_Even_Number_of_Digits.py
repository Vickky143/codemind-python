a=int(input())
lst=list(map(int,input().split()))
c=0
for i in lst:
    m=len(str(i))
    if m%2==0:
        c+=1
print(c)