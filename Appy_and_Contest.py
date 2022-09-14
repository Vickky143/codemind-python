n=int(input())
for i in range(n):
    a,b,c,d=map(int,input().split())
    b=a//b
    c=a//c
    if (b+c)>=d:
        print("Win")
    else:
        print("Lose")