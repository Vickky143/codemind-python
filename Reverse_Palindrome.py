n=int(input())
x=n
sum=0
while n>0:
    a=n%10
    sum=sum*10+a
    n=n//10
k=sum+x
v=k
count=0
while k>0:
    b=k%10
    count=count*10+b
    k=k//10
    if count!=v and k==0:
        k=count+v
        v+=count
        count=0
if v==count:
    print(v)