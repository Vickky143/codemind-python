a,b,c=map(int,input().split())
s=(a+b+c)/2
d=s-a
e=s-b
f=s-c
g=d*e*f
h=s*g
l=h**0.5
print("{:.2f}".format(l))