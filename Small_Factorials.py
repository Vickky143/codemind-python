t=int(input())
for i in range(t):
    a=int(input())
    mul=1
    for n in range(a,1,-1):
        mul=mul*n
    print(mul)