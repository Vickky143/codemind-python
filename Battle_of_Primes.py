a=int(input())
b=int(input())
c=a+b+1
while 1:
    prime=True
    for i in range(2,int(c**0.5)+1):
        if c%i==0:
            prime=False
            break
    if prime==True:
        break
    else:
        c+=1
print(c-(a+b))