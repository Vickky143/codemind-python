n=int(input())
m=list(map(int,input().split()))
v=0
for i in range(0,len(m),2):
    if m[i]%2!=0:
        v=0
    else:
        v=1
if v==1:
    print('True')
else:
    print('False')