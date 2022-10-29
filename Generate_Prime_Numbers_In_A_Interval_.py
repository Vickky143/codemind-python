a=int(input())
b=int(input())
k=[]
for i in range(a,b+1):
    v=1
    for j in range(2,int(i**0.5)+1):
        if i%j==0:
            v=2
            break
    if v==1:
        k.append(i)
if 1 in k:
    k.remove(1)
    for i in k:
        print(i)
else:
    for i in k:
        print(i)