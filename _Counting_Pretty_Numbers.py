n=int(input())
for i in range(n):
    a,b=map(int,input().split())
    count=0
    for m in range(a,b+1):
        m=m%10
        if m==3 or m==2 or m==9:
            count+=1
    print(count)