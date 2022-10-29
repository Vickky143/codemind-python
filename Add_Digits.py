a=int(input())
sum=0
while a>0:
    n=a%10
    sum=sum+n
    a=a//10
    if sum>9 and a==0:
        a=sum
        sum=0
else:
    print(sum)