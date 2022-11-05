n=int(input())
m=list(map(int,input().split()))
k=(sum(m)/len(m))
print('{:.2f}'.format(k))