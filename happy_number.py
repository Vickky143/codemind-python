n=int(input())
sum=0
while n>0:
    a=n%10
    sum=sum+a*a
    n=n//10
    if sum>9 and n==0:
        n=sum
        sum=0
if sum==1 or sum==7:
    print('True')
else:
    print("False")