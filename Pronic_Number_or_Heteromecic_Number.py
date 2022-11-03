n=int(input())
m=int(n**0.5)
for i in range(1,m+1):
    x=i*(i+1)
    if x==n:
        print("YES")
        break
else:
    print("NO")