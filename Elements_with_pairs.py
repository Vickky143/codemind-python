n=int(input())
m=list(map(int,input().split()))
for i in m:
    if len(m)%2==0:
        print(i,end=' ')
    else:
        m.insert(len(m),0)
        print(i,end=' ')