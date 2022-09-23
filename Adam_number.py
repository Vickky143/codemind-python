n=int(input())
m=n*n
sum =0
mul=0
while n>0:
    r=n%10
    sum=(sum*10)+r
    n=n//10
z=sum*sum
while z>0:
    k=z%10
    mul=mul*10+k
    z=z//10
if m==mul:
    print("True")
else:
    print("False")