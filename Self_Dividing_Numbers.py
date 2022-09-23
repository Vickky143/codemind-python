n=int(input())
m=int(input())
for i in range(n,m+1):
    k=i
    while i>0:
        b=i%10
        i=i//10
        if b==0:
            break
        elif k%b!=0:
            break
    else:
        print(k,end=" ")
