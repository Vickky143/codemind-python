n=int(input())
m=list(map(int,input().split()))
k=int(sum(m)/len(m))
if k in m:
    print('True')
else:
    print('False')