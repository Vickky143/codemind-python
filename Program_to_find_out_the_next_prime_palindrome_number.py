def ant(n):
    v=1
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            v=2
            break
    return v
    
def want(n):
    sum=0
    while n>0:
        a=n%10
        sum=sum*10+a
        n=n//10
    return sum

n=int(input())
n+=1
while want(n)!=n or ant(n)!=1:
    n+=1
print(n)