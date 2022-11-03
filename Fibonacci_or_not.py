t=int(input())
k=[0]*t
for i in range(1,len(k)):
    k[1]=1
    for i in range(2,len(k)):
        k[i]=k[i-1]+k[i-2]
if t in k:
    print("True")
else:
    print("False")