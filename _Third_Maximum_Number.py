a=int(input())
b=list(map(int,input().split()))
v=set(b)
m=sorted(v)
n=len(m)-3
print(m[n])