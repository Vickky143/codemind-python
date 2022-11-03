n=int(input())
m=n*n
k=len(str(n))
v=m%10**k
if v==n:
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")