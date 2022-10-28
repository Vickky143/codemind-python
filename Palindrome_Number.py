for i in range(int(input())):
    n=int(input())
    m=n
    sum=0
    while n>0:
        a=n%10
        sum=sum*10+a
        n=n//10
    if sum==m:
        print("True")
    else:
        print("False")