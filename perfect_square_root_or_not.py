import math
n=int(input())
m=n**0.5
res=math.ceil(m)
if res*res==n:
    print("True")
else:
    print("False")