def wow(w):
    m=n+1
    k=m
    sum=0
    while m>0:
        a=m%10
        sum=sum*10+a
        m=m//10
        if sum!=k and m==0:
            m=k+1
            k+=1
            sum=0
    return sum
def ant(w):
    x=n-1
    s=x
    z=0
    while x>0:
        c=x%10
        z=z*10+c
        x=x//10
        if z!=s and x==0:
            x=s-1
            s-=1
            z=0
    return z
n=int(input())
if (wow(n)-n)==(n-ant(n)):
    print(ant(n),wow(n))
elif (wow(n)-n)>(n-ant(n)):
    print(ant(n))
else:
    print(wow(n))