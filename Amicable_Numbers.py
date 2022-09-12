a=int(input())
b=int(input())
sum=0
for i in range(1,a):
    if a%i==0:
        sum=sum+i
mul=0
for n in range(1,b):
    if b%n==0:
        mul=mul+n
if sum==b and mul==a:
    print("Amicable")
else:
    print("Not Amicable")