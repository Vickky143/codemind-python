n=int(input())
u=n
m=n*n
sum=0
while m>0:
    r=m%10
    sum=sum+r
    m=m//10
if sum==n:
    print("Neon Number")
else:
    print("Not Neon Number")