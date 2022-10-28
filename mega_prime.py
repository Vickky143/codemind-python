m=int(input())
n=1
for i in range(2,int(m**0.5)+1):
    if m%i==0:
        n=2
        break
k=str(m)
j=1
for i in k:
    for d in range(2,int(int(i)**0.5)+1):
        if int(i)%d==0:
            j=2
            break
if '1' in k:
    print("Not Mega Prime")
elif n==1 and j==1:
    print("Mega Prime")
else:
    print("Not Mega Prime")