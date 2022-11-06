n=int(input())
m=list(map(int,input().split()))
v=0
for i in m:
    if i%2==0:
        v+=1
if v==len(m):
    print('True')
else:
    print('False')