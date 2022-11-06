n=int(input())
m=list(map(int,input().split()))
v=0
for i in range(1,len(m),2):
    if m[i]%2==0:
        v=1 
    else:
        v=0
if v==0:
    print('True')
else:
    print('False')