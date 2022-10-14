t=int(input())
for g in range(t):
    n=int(input())
    m=n
    while 1:
        k=0
        for i in range(2,int(m**0.5)+1):
            if m%i==0:
                k=1
                break
        if k==0:
            break
        else:
            m=m-1
    
    v=n
    while 1:
        b=2
        for i in range(2,int(v**0.5)+1):
            if v%i==0:
                b=3
                break
        if b==2:
            break
        else:
            v=v+1
    j=n-m
    d=v-n
    if d<j:
        print(v)
    else:
        print(m)